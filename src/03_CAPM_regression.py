import pandas as pd
import statsmodels.api as sm

#read data
df = pd.read_csv('C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\data\\processed\\capm_data.csv', index_col=0, parse_dates=True)

results = []
stock_list = [col for col in df.columns if col.endswith('_RF')]

for stock in stock_list:
    ticker = stock.replace('_RF', '')
    Y = df[stock]        # market excess return for the stock
    X = df['Mkt_RF']     # market excess return
    X = sm.add_constant(X)  # add constant term (alpha)
    
    model = sm.OLS(Y, X).fit()
    
    results.append({
        'Ticker': ticker,
        'Alpha': model.params['const'],
        'Beta': model.params['Mkt_RF'],
        'R-squared': model.rsquared,
        'p-value (Alpha)': model.pvalues['const'],
        'p-value (Beta)': model.pvalues['Mkt_RF']
    })

summary_df = pd.DataFrame(results).set_index('Ticker')
summary_df.to_csv('C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\output\\tables\\capm_summary.csv')
print(summary_df)