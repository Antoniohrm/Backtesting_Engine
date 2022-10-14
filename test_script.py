import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from Backtest import test

prices = pd.read_csv('test_data/Binance_BTCUSD.csv', index_col = 'unix')
prices = prices[['open', 'high', 'low', 'close']]

# Dates in [year, month, day, hour, minute] format
start = [2022, 1, 1, 12, 0]
end = [2022, 2, 1, 12, 0]
dt = 3600

Result, ret = test(prices, start, end, dt)
print(ret)