import numpy as np

def optimize_portfolio(returns):

    weights = np.ones(len(returns))/len(returns)

    portfolio_return = np.sum(returns.mean()*weights)

    return portfolio_return
