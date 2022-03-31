import pandas as pd
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
import YJDownloadNikkei50Prices



def OptimizePortfolio(prices):
    mu = expected_returns.mean_historical_return(prices)
    S = risk_models.sample_cov(prices)
    # Optimize for maximal Sharpe ratio
    ef = EfficientFrontier(mu, S)
    raw_weights = ef.max_sharpe()
    cleaned_weights = ef.clean_weights()
    ef.save_weights_to_file("weights.csv")  # saves to file
    print(cleaned_weights)
    ef.portfolio_performance(verbose=True)

def formatNikkeiPricesCSC(prices):
    return


# Read in price data
stockprices = pd.read_csv("data/nikkei50.csv", parse_dates=True, index_col="date")
stockprices = YJDownloadNikkei50Prices.FixFormat(stockprices)

print(stockprices.head())

OptimizePortfolio(stockprices)



