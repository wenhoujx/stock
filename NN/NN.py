import numpy as np 
import utils.data_processing as dp
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer

if __name__=='__main__':
    prices, tickers = dp.loaddata()
    prices = dp.normalization(prices)

    fnn = buildNetwork(prices.shape[1], 100, 10, 
    
