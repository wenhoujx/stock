import numpy as np 


def loaddata(): 
    prices , labels = (np.load('../data/valid_prices') , np.load('../data/valid_labels'))
    prices = prices.astype(np.float)
    # delete rows with all zeros
    prices = prices[ ~ np.all( prices==0, axis=1)]
    return prices , labels


def normalization(prices):
    # prices /= prices.max(axis=1)[:, None]
    # norm = 1 
    prices /= np.apply_along_axis( np.linalg.norm, axis = 1 , arr = prices)[:,None]
    return prices
    
