# Contrarian Trading Strategy

Python implementation of a contrarian (mean reversion) trading strategy with backtesting support.

## Strategy Logic
- Enter long when price is significantly below N-day moving average
- Enter short when price is significantly above N-day moving average
- Exit on mean reversion or stop-loss

## Requirements
```
pip install pandas numpy matplotlib backtrader yfinance
```

## Usage
```bash
python backtest.py --ticker SPY --start 2020-01-01 --end 2024-01-01
```

## Configuration
Edit `config.py` to adjust lookback period, threshold multiplier, and position sizing.

## License
MIT
<!-- updated: 2024-10-12-r01 -->
