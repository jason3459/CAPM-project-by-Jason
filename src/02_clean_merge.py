import pandas as pd
import numpy as np

#data
prices = pd.read_csv('C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\data\\raw\\stock_prices.csv', index_col=0, parse_dates=True)
rf_annual = pd.read_csv('C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\data\\raw\\risk_free_rate.csv', index_col=0, parse_dates=True)

rf_daily = rf_annual / 252
rf_daily.columns = ['RF']

returns = prices.pct_change().dropna()

#join returns and risk-free rate
df = returns.join(rf_daily, how='inner').dropna()

#profits
df['Mkt_RF'] = df['^GSPC'] - df['RF']
for ticker in prices.columns:
    if ticker != '^GSPC':
        df[f'{ticker}_RF'] = df[ticker] - df['RF']

df.to_csv('C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\data\\processed\\capm_data.csv')
print("clean_merge completed. Data saved to processed folder.")
print(df.head())