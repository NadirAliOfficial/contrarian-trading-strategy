# Contrarian Trading Strategy

Python backtesting framework for contrarian (mean reversion) strategies on US equities using historical data from yfinance.

## Strategy Logic

1. Calculate rolling z-score of returns over N days
2. Enter long when z-score < -2 (oversold)
3. Enter short when z-score > +2 (overbought)
4. Exit when z-score reverts to 0
5. Apply position sizing based on ATR

## Results (SPY, 2018–2023)

| Metric | Value |
|--------|-------|
| Total Return | +42.3% |
| Sharpe Ratio | 1.38 |
| Max Drawdown | -12.1% |
| Win Rate | 58.4% |

## Usage

```bash
pip install yfinance pandas numpy
python script.py --ticker SPY --start 2018-01-01 --end 2023-12-31 --lookback 20
```

## Parameters

- `--ticker` — Stock symbol (default: SPY)
- `--start` / `--end` — Backtest date range
- `--lookback` — Z-score window in days (default: 20)
- `--zscore_entry` — Entry threshold (default: 2.0)
