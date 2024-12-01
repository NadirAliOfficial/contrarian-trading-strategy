import yfinance as yf
import numpy as np
import pandas as pd

class ContrarianStrategy:
    def __init__(self, data, start_balance=10000):
        self.data = data
        self.trades = []
        self.balance = start_balance
        self.equity_curve = []
    
    def enter_trade(self, condition, price):
        # Handle condition if it's a Series to avoid ambiguity
        if isinstance(condition, pd.Series):
            condition = condition.iloc[0]  # Check the first value if it's a Series
        if condition:
            self.trades.append({"type": "buy", "price": price, "size": 1})
            self.balance -= price
    
    def exit_trade(self, condition, price):
        # Handle condition if it's a Series to avoid ambiguity
        if isinstance(condition, pd.Series):
            condition = condition.iloc[0]  # Check the first value if it's a Series
        if condition and self.trades:
            trade = self.trades.pop(0)
            profit = (price - trade["price"]) * trade["size"]
            self.balance += price * trade["size"]
            return profit
        return 0
    
    def backtest(self, entry_drop=1.0, averaging_drop=2.0, exit_gain=1.0):
        profits = []
        for i, row in self.data.iterrows():
            # Get OHLC data
            open_price = row['Open']
            low_price = row['Low']
            high_price = row['High']
            close_price = row['Close']

            # Simulate entering trade
            if not self.trades:
                condition = low_price < open_price * (1 - entry_drop / 100)
                self.enter_trade(condition, low_price)
            elif self.trades:
                # Simulate averaging down
                avg_price = np.mean([trade['price'] for trade in self.trades])
                condition = low_price < avg_price * (1 - averaging_drop / 100)
                self.enter_trade(condition, low_price)
            
            # Simulate exiting trade
            if self.trades:
                avg_price = np.mean([trade['price'] for trade in self.trades])
                profit = self.exit_trade(high_price > avg_price * (1 + exit_gain / 100), high_price)
                # Ensure profit is a scalar value before checking
                if isinstance(profit, pd.Series):
                    profit = profit.iloc[0]  # If profit is a Series, get the first value
                if profit:
                    profits.append(profit)

            # Record equity curve
            self.equity_curve.append(self.balance + sum(trade["price"] for trade in self.trades))

        return profits
    
    def analyze_performance(self, profits):
        profits = np.array(profits)
        total_profit = np.sum(profits)
        drawdown = np.min(np.cumsum(profits)) if len(profits) > 0 else 0
        win_rate = np.mean(profits > 0) if len(profits) > 0 else 0
        sharpe_ratio = np.mean(profits) / np.std(profits) if len(profits) > 0 else 0
        
        return {
            "Total Profit": total_profit,
            "Max Drawdown": drawdown,
            "Win Rate": win_rate,
            "Sharpe Ratio": sharpe_ratio
        }


def fetch_intraday_data(ticker, interval="1d", start_date="2024-01-01", end_date="2024-01-28"):
    """
    Fetch intraday stock data using yfinance.
    """
    data = yf.download(ticker, interval=interval, start=start_date, end=end_date)
    return data


if __name__ == "__main__":
    # Step 1: Fetch data
    ticker = "AAPL"
    interval = "1d"
    start_date = "2024-01-01"
    end_date = "2024-01-28"
    print("Fetching data...")
    data = fetch_intraday_data(ticker, interval, start_date, end_date)
    
    # Ensure data is not empty
    if data.empty:
        print("No data fetched. Check your ticker symbol or date range.")
    else:
        # Step 2: Initialize and run backtesting
        print("Running backtest...")
        strategy = ContrarianStrategy(data)
        profits = strategy.backtest()

        # Step 3: Analyze performance
        performance = strategy.analyze_performance(profits)
        equity_curve = pd.DataFrame({"Equity": strategy.equity_curve})

        print("\nPerformance Metrics:")
        for metric, value in performance.items():
            print(f"{metric}: {value}")

        # Step 4: Save results
        equity_curve.to_csv("equity_curve.csv", index=False)
        print("\nEquity curve saved to 'equity_curve.csv'")
