import numpy as np
import pandas as pd
import datetime
import time

from Strategy import strategy

def prepareDate(date):
    date_datetime = datetime.datetime(date[0], date[1], date[2], date[3], date[4])
    unix_epoch = int(time.mktime(date_datetime.timetuple()))
    return unix_epoch

def updatePortfolio(action, amount, price):
    cash -= (action * amount)
    asset += ((amount / price) * action)
    portfolio_value = cash + (asset * price)

    return [cash, asset, portfolio_value]

def test(prices, start, end, dt = (60 * 60)):
    t0 = prepareDate(start)
    tf = prepareDate(end)
    t = t0 + dt

    portfolio = [1000, 0, 1000]
    res = []

    while t < tf:
        price = prices.loc[t, 'close']
        action, amount = strategy(price, portfolio)
        if (action == 1) and (portfolio[0] < amount):
            amount = portfolio[0]
        else if (action == -1) and (portfolio[1] < (price * portfolio[1])):
            amount = (price * portfolio[1])
        portfolio = updatePortfolio(action, amount, price)
        res.append(portfolio)
        t += tf
    
    Res = pd.DataFrame(res)

    return Res