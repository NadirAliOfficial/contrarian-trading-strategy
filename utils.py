import pandas as pd
import numpy as np

def compute_zscore(series, window=20):
    mean = series.rolling(window).mean()
    std  = series.rolling(window).std()
    return (series - mean) / std

def compute_atr(high, low, close, period=14):
    tr = pd.concat([
        high - low,
        (high - close.shift()).abs(),
        (low  - close.shift()).abs()
    ], axis=1).max(axis=1)
    return tr.rolling(period).mean()

def sharpe_ratio(returns, risk_free=0.0, periods=252):
    excess = returns - risk_free / periods
    return np.sqrt(periods) * excess.mean() / excess.std()

def max_drawdown(equity_curve):
    roll_max = equity_curve.cummax()
    drawdown = equity_curve / roll_max - 1
    return drawdown.min()

def print_stats(returns, label="Strategy"):
    equity = (1 + returns).cumprod()
    print(f"\n=== {label} ===")
    print(f"  Total Return : {(equity.iloc[-1]-1)*100:.2f}%")
    print(f"  Sharpe Ratio : {sharpe_ratio(returns):.2f}")
    print(f"  Max Drawdown : {max_drawdown(equity)*100:.2f}%")
    print(f"  Win Rate     : {(returns > 0).mean()*100:.1f}%")
