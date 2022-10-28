import numpy as np
import pandas as pd
import math
import datetime as dt
import pandas_datareader as web

def get_Yahoo_data_ES50(tickers_ES50):
  start = dt.datetime(2016,1,1)
  end = dt.datetime(2022,9,1)
  f = web.DataReader(tickers_ES50, 'yahoo', start, end)
  f = pd.DataFrame(f)

  f.to_csv('../data/raw/ES50.csv')

  return f

def get_Yahoo_data_ndx(ticker_ndx):
  start = dt.datetime(2016,1,1)
  end = dt.datetime(2022,9,1)
  f = web.DataReader(ticker_ndx, 'yahoo', start, end)
  f = pd.DataFrame(f)

  f.to_csv('../data/raw/ES50_index.csv')

  return f

def get_log_returns(f):
    closing_prices = f
    closing_prices.fillna(np.nan, inplace=True)
    dates = closing_prices.iloc[:,0]
    closing_prices = closing_prices.iloc[: , 1:]
    columns_names = closing_prices.columns.tolist()
    df_log_returns = np.log(closing_prices) - np.log(closing_prices.shift(1))
    df_log_returns['Date'] = dates
    df_log_returns = df_log_returns[['Date'] + columns_names]
    df_log_returns = df_log_returns.iloc[1:,:]
    return df_log_returns

def get_cumulative_returns(returns):
  return np.exp(returns.cumsum())