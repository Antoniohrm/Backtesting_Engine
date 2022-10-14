import numpy as np
import pandas as pd
import datetime
import time

from basic_strat import strategy

prices = pd.read_csv('test_data/Binance_BTCUSD.csv', index_col = 'unix')
prices = prices[['open', 'high', 'low', 'close']]

# Dates in [year, month, day, hour, minute] format
start = [2022, 1, 1, 12, 0]
end = [2022, 6, 1, 12, 0]

start_date = datetime.datetime(start[0], start[1], start[2], start[3], start[4])
end_date = datetime.datetime(end[0], end[1], end[2], end[3], end[4])

def updatePV(action, amount, price = prices.loc[t, 'close']):
    cash -= (action * amount)
    asset += ((amount / price) * action)
    portfolio_value = cash + (asset * price)

    return [cash, asset, portfolio_value]

def test(start_date = start_date, end_date = end_date, dt = (60 * 60)):
    t0 = int(time.mktime(start_date.timetuple()))
    tf = int(time.mktime(end_date.timetuple()))
    t = t0 + dt

    portfolio = [1000, 0, 1000]
    res = pd.DataFrame()

    while t < tf:
        action, amount = strategy(prices.loc[t0:t], portfolio)
        price = prices.loc[t, 'close']
        if (action == 1) and (portfolio[0] < amount):
            amount = portfolio[0]
        else if (action == -1) and (portfolio[1] < (price * portfolio[1])):
            amount = (price * portfolio[1])
        
        


test()