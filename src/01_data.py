import yfinance as yf
import pandas as pd
import os

tickers=['AAPL','MSFT','GOOGL','AMZN','TSLA','NVDA','MCD','HPQ','ABNB','BA']
market_ticker='^GSPC'  # S&P 500 index
start_date='2021-01-01'
end_date='2026-01-01'

print('Downloading data for tickers:', tickers)
print('Downloading data for market ticker:', market_ticker)
data=yf.download(tickers+[market_ticker], start=start_date, end=end_date,auto_adjust=True
               )['Close']

import pandas_datareader.data as web
rf_annual = web.DataReader('DTB3', 'fred', start_date, end_date)
rf_annual = rf_annual/100

os.makedirs('C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\data\\raw', exist_ok=True)
data.to_csv('C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\data\\raw\\stock_prices.csv')
rf_annual.to_csv('C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\data\\raw\\risk_free_rate.csv')

print('Download completed. Data saved to raw folder.')
print(data.head())
