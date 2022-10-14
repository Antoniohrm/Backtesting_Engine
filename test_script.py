import numpy as np
import pandas as pd

from Backtest import test

prices = pd.read_csv('test_data/Binance_BTCUSD.csv', index_col = 'unix')
prices = prices[['open', 'high', 'low', 'close']]

# Dates in [year, month, day, hour, minute] format
start = [2022, 1, 1, 12, 0]
end = [2022, 6, 1, 12, 0]