CAPM Analysis of 10 US stocks

1. Introduction
- What is CAPM?:
The capital asset pricing model (CAPM) is a model used to determine the expected return of an investment based on its market risk.
The formula for calculating the expected return of an asset, given its risk, is as follows:E_Ri=Rf+β_i(E_Rm-Rf),
​where E_Ri is expected return of investment,
Rf is risk_free rate,
β_i is beta of investment,
E_Rm-Rf is market risk premium.

- Why are we testing it?:
The goal of the CAPM formula is to evaluate whether a stock is fairly valued when its risk and the time value of money are compared with its expected return. In other words, by knowing the individual parts of the CAPM, it is possible to gauge whether the current price of a stock is consistent with its likely return.

2. Data
- 10 stock:
AAPL ABNB AMZN BA GOOGL HPQ	MCD	MSFT NVDA TSLA

- S&P 500:
^GSPC

- risk-free rate:
The risk-free rate used in this project is the DTB3 series from the FRED database, which represents the 3-Month U.S. Treasury Bill secondary market rate on a discount basis. The raw data is annualized and expressed as a percentage. It was converted into a daily decimal form by dividing by 100 and then by 252, in order to match the frequency of the daily stock returns.

- time period:
1/1/2021 - 1/1/2026

- daily/monthly frequency:
daily frequency​

3. Methodology
- return calculation:
Daily simple returns were calculated for all stocks and the S&P 500 index using the formula: 
R_t=(P_t−P_t−1)/P_t−1​
where P_t is the adjusted closing price on day t. Adjusted closing prices were used to account for dividends and stock splits, ensuring the returns reflect total shareholder value.

- excess return calculation:
The risk-free rate was obtained from the FRED database (series DTB3, the 3-Month U.S. Treasury Bill rate). The annualized rate was converted to a daily rate by dividing by 100 (to convert from percentage to decimal) and then by 252 (the approximate number of trading days in a year).

Excess returns were then computed as:

Stock excess return: R_it−R_ft;
Market excess return: R_mt-R_ft;
where R_it is the return of stock i, R_mt is the return of the S&P 500, and R_ft is the daily risk-free rate.

- CAPM calculation:
"In the theoretical CAPM equation, there is no alpha term because the model assumes that expected returns are fully explained by market risk. However, in the empirical regression specification R_it−R_ft=α_i+β_i(R_mt−R_ft)+ϵ_it, 
α_i represents the intercept. A statistically significant positive alpha indicates that the stock has outperformed the market beyond what its beta exposure would predict, suggesting either market inefficiency or the omission of other risk factors."

- OLS regression:
Ordinary Least Squares (OLS) regression was performed for each of the 10 stocks using the statsmodels library in Python. For each stock, we obtained estimates of alpha, beta, their corresponding p-values, and the R-squared value.

4 Results
- alpha:
The estimated alpha values ranged from -0.0002 to 0.002(3 d.p.). A positive alpha indicates that the stock outperformed the market after adjusting for risk, while a negative alpha suggests underperformance. Statistically significant alphas (p < 0.05) were found for all stocks.

- beta:
The estimated beta values ranged from 0.414 to 2.165(3 d.p.). Stocks with beta greater than 1 include Tesla and Nvidia, indicating they are more volatile than the market (aggressive stocks). Stocks with beta less than 1 include Mcdonald's, indicating they are less volatile than the market (defensive stocks). For example, Tesla had the highest beta of 2.165, while Mcdonald's had the lowest beta of 0.414.

- R-squared:
The R-squared values ranged from 0.168 to 0.580(3 d.p.). A higher R-squared indicates that a larger proportion of the stock's return variation is explained by market movements. Microsoft had the highest R-squared of 0.580, suggesting it is highly correlated with the market. Mcdonald's had the lowest R-squared of 0.168, suggesting that other factors play a significant role in its return.

- p-values:
The p-values for beta were statistically significant (p < 0.05) for all 10 stocks, confirming that market returns are a significant driver of individual stock returns. For alpha, only 1 stock had p-values below 0.05, indicating that for most stocks, the abnormal return is not statistically distinguishable from zero.

5. Graphical Analysis
- Beta comparison:
The bar chart of betas(../outputs/figurs/beta_comparison.png) visually compares the systematic risk of all 10 stocks. The red dashed line at beta = 1 serves as a reference. Stocks to the above of this line are more volatile than the market, while those to the below are less volatile. 

- Scatter/regression plots:
For each stock, a scatter plot of stock excess returns against market excess returns was generated, with the OLS regression line overlaid. These plots(../output/figures) show a positive linear relationship, consistent with CAPM theory. The slope of the line represents the beta, and the intercept represents the alpha.

- Residual plots:
Residual plots (../output/figures) show the residuals plotted against fitted values. Ideally, residuals should be randomly scattered around zero with no discernible pattern. For most stocks, the residuals appear randomly distributed, suggesting the linear model is appropriate. 

- Rolling beta:
The rolling beta charts (../output/figures) show how beta changes over time using a 60-day rolling window. For most stocks, beta is not constant. Notably, during periods of market stress (e.g. the 2022 interest rate hikes), betas tended to decrease for many stocks, indicating that systematic risk is time-varying.

6. Discussion
- Beta differences:
The results show clear differences in beta across industries. Tesla had the highest beta, consistent with its high-growth, volatile nature. Mcdonald's had the lowest beta, consistent with its defensive characteristics. This supports the hypothesis that defensive stocks have lower betas.

- Alpha significance:
Only 1 stock had statistically significant alphas. This suggests that for most stocks, the CAPM model adequately explains returns, and there is no evidence of abnormal performance. However, for Nvidia, the significant alpha may indicate mispricing or exposure to risk factors not captured by the market factor alone.

- Model explanatory power:
R-squared values varied considerably. Stocks with high R-squared (e.g. Microsoft) are highly sensitive to market movements, while those with low R-squared (e.g. Mcdonald's) are driven more by idiosyncratic factors. This implies that CAPM is a better model for some stocks than others.

- Beta stability:
The rolling beta analysis shows that beta is not stable over time. For many stocks, beta fluctuated significantly, especially during periods of market turbulence. This challenges the CAPM assumption of a constant beta and suggests that risk exposure changes over time.

- Residual behavior:
Residual plots show that residuals are generally centered around zero, but some stocks exhibit non-normal residuals or heteroscedasticity. This violates the OLS assumptions and may affect the reliability of standard errors and hypothesis tests

7. Limitations
- CAPM uses only one market factor:
CAPM assumes that market risk is the only systematic risk factor. In reality, other factors such as size, value, momentum, and profitability also affect returns. This limitation may explain why some stocks have significant alphas.

- Results depend on time period:
The choice of time period (2021–2026) significantly affects the results. Different periods may yield different beta and alpha estimates, especially during market crises or structural changes.

- Results may differ with daily vs monthly data:
Using daily data captures more noise and short-term fluctuations, while monthly data smooths out noise but reduces the number of observations. Conclusions about beta stability and alpha significance may differ depending on the frequency chosen.

8. Conclusion:
This project applied the Capital Asset Pricing Model to 10 U.S. stocks from different industries. The results show that betas vary widely across stocks, with technology and growth stocks exhibiting higher betas than defensive stocks. Most stocks had statistically insignificant alphas, suggesting that market risk is the primary driver of returns. However, the rolling beta analysis revealed that beta is not constant over time, and residual diagnostics indicated some violations of OLS assumptions.
Overall, CAPM provides a useful but incomplete framework for understanding stock returns. Future research could incorporate multi-factor models (e.g., Fama-French three-factor model) and consider different time frequencies to gain a more comprehensive understanding of risk and return.
