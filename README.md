# Contrarian Trading Strategy

This project implements a **Contrarian Trading Strategy** using Python to backtest and evaluate a trading approach based on market reversals. The strategy involves entering positions when the market shows signs of price drops (entry), averaging down on further declines (averaging), and exiting the position once the price reaches a specific target (exit).

The implementation uses historical stock data fetched via the **yfinance** library to simulate the trades and analyze the performance of the strategy.

## Features
- **Backtesting:** The strategy is backtested using historical stock data. It simulates entering, averaging, and exiting trades based on predefined conditions.
- **Profit Calculation:** Profits from trades are calculated dynamically as per the trade size and entry/exit prices.
- **Performance Metrics:** After backtesting, various performance metrics like total profit, drawdown, win rate, and Sharpe ratio are computed to evaluate the strategy's effectiveness.

## Strategy Details
- **Entry Condition:** A trade is entered if the stock price drops a certain percentage from the opening price (entry drop).
- **Averaging Down:** If the price continues to drop, additional positions are taken at a lower price (averaging drop).
- **Exit Condition:** The position is exited when the price increases by a predefined percentage from the average price (exit gain).

## Requirements
- Python 3.x
- `yfinance` library for fetching stock data
- `numpy` and `pandas` for numerical and data manipulation

You can install the required libraries by running:

```bash
pip install yfinance numpy pandas
```

## Usage

1. **Fetch Intraday Data:** The `fetch_intraday_data` function fetches stock data using **yfinance**.
2. **Backtest the Strategy:** The `ContrarianStrategy` class implements the strategy and runs the backtest on the fetched data.
3. **Analyze Results:** The performance metrics such as Total Profit, Max Drawdown, Win Rate, and Sharpe Ratio are printed after running the backtest.
4. **Equity Curve:** The equity curve over time is saved to a CSV file for further analysis.

## Example

```python
from contrarian_strategy import ContrarianStrategy, fetch_intraday_data

# Fetch data
data = fetch_intraday_data('MSFT', start_date='2024-01-01', end_date='2024-01-28')

# Initialize the strategy
strategy = ContrarianStrategy(data)

# Run the backtest
profits = strategy.backtest()

# Analyze performance
performance = strategy.analyze_performance(profits)
print(performance)

# Save equity curve
strategy.save_equity_curve('equity_curve.csv')
```

## Contributing

Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests.

## License

This project is licensed under the MIT License.
