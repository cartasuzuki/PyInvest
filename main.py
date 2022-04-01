import pandas as pd
import PortfolioOptimizer
import YJDownloadNikkei50Prices






# Read in price data
stockprices = pd.read_csv("data/nikkei50.csv", parse_dates=True, index_col="date")
stockprices = YJDownloadNikkei50Prices.FixFormat(stockprices)

print(stockprices.head())

weights, sharpe, ret = PortfolioOptimizer.PortfolioOptimizer.optimize_portfolio(stockprices,0,0.25)



