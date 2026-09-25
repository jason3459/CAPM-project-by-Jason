import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

#read data
df = pd.read_csv('C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\data\\processed\\capm_data.csv', index_col=0, parse_dates=True)
stock_list = [col for col in df.columns if col.endswith('_RF')]

#scatter plot+regression line for each stock
print("plotting scatter plots...")
for stock in stock_list:
    ticker = stock.replace('_RF', '')
    plt.figure(figsize=(8, 6))
    sns.regplot(x=df['Mkt_RF'], y=df[stock], 
                line_kws={'color': 'red', 'label': 'Regression Line'}, 
                scatter_kws={'alpha': 0.5, 's': 20})
    plt.title(f'{ticker} Excess Returns vs Market Excess Returns', fontsize=14)
    plt.xlabel('Market Excess Return (Mkt_RF)', fontsize=12)
    plt.ylabel(f'{ticker} Excess Return', fontsize=12)
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\output\\figures\\{ticker}_scatter.png', dpi=300)
    plt.close() 


#compare betas across stocks
print("plotting beta comparison...")
summary = pd.read_csv('C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\output\\tables\\capm_summary.csv', index_col=0)
plt.figure(figsize=(10, 6))
summary['Beta'].plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('CAPM Beta Comparison Across Stocks', fontsize=14)
plt.xlabel('Stock Ticker', fontsize=12)
plt.ylabel('Beta', fontsize=12)
plt.axhline(1, color='red', linestyle='--', linewidth=1.5, label='Beta = 1')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\output\\figures\\beta_comparison.png', dpi=300)
plt.close()

#rolling beta plot
print("plotting rolling beta plots...")
window = 60
for stock in stock_list:
    ticker = stock.replace('_RF', '')
    rolling_betas = []
    for i in range(window, len(df)):
        sub = df.iloc[i-window:i]
        X = sm.add_constant(sub['Mkt_RF'])
        model = sm.OLS(sub[stock], X).fit()
        rolling_betas.append(model.params['Mkt_RF'])
    
    plt.figure(figsize=(10, 6))
    plt.plot(df.index[window:], rolling_betas, color='darkblue', linewidth=1.5)
    plt.title(f'Rolling Beta (60-day Window) for {ticker}', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Beta', fontsize=12)
    plt.axhline(1, color='red', linestyle='--', linewidth=1, label='Beta = 1')
    plt.legend()
    plt.tight_layout()
    plt.savefig(f'C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\output\\figures\\{ticker}_rolling_beta.png', dpi=300)
    plt.close()

#residual plots
print("plotting residual plots...")
for stock in stock_list:
    ticker = stock.replace('_RF', '')
    X = sm.add_constant(df['Mkt_RF'])
    model = sm.OLS(df[stock], X).fit()
    residuals = model.resid
    fitted = model.fittedvalues

    plt.figure(figsize=(8, 6))
    plt.scatter(fitted, residuals, alpha=0.5, s=20, color='purple')
    plt.axhline(0, color='red', linestyle='--', linewidth=1.5)
    plt.title(f'Residual Plot for {ticker}', fontsize=14)
    plt.xlabel('Fitted Values', fontsize=12)
    plt.ylabel('Residuals', fontsize=12)
    plt.tight_layout()
    plt.savefig(f'C:\\Users\\jason\\Desktop\\OSG related\\coding\\capm project\\output\\figures\\{ticker}_residuals.png', dpi=300)
    plt.close()

print("all plots generated and saved to output/figures folder.")