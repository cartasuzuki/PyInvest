#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:40:58 2018

@author: carlo
"""

import pandas as pd
from pypfopt.efficient_frontier import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
import numpy as np
import matplotlib.pyplot as plt

class PortfolioOptimizer:
    
    
   
    def optimize_portfolio(stocks, min_allocation, max_allocation=1):
        exp_ret = -expected_returns.mean_historical_return(stocks)
        S = risk_models.sample_cov(stocks)
    
        ef = EfficientFrontier(exp_ret, S, weight_bounds = (min_allocation,max_allocation))
        weights = ef.max_sharpe()
        ret, vol, sharpe = ef.portfolio_performance(verbose=False)
        return(weights, sharpe, ret)
        
    def print_portfolio_result(weights, sharpe, ret):
        for s in weights:
            weights[s] = round(weights[s],2)
            ss = s + ": " + str(weights[s]*100) + "%"
            if(weights[s] > 0.04):
                print(ss)
        print("Sharpe: " + str(round(sharpe,2)) )
        print("Exp. Return: " + str(round(ret*100,2)) )

    def portfolioAsPieChart(weights):
        symbolList = []
        weightList = []
        for s, w in weights.items():
            tempS = s
            tempW = w
            if(tempW > 0.001):
                symbolList.append(tempS)
                weightList.append(tempW)
    
        weightArray = np.array(weightList)
        plt.pie(x = weightArray, labels = symbolList)
        
    def expected_returns_and_cov(stocks):
        exp_ret = -expected_returns.mean_historical_return(stocks)
        S = risk_models.sample_cov(stocks)
        print("Cov: " + str(round(S,2)) )
        print("Exp. Return: " + str(round(exp_ret*100,2)) )
            
