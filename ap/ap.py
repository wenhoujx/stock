from sklearn.cluster import AffinityPropagation
import numpy as np 
from sklearn import metrics
import utils.data_processing as dp 
import itertools as it 
import pylab as pl

def plot_eachclass(prices, af):
    center_idx = af.cluster_centers_indices_
    lbls = af.labels_

    for i in range(len(np.unique(lbls))):
        p = prices[np.where(lbls == i)]
        N = 100
        if N > len(p):
            N = len(p)

        p = p[np.random.randint( 0 , len(p), N)]
        for y, c , ls in zip( p , it.cycle('bgrcmyk') , it.cycle('_-:')):
            pl.plot(xrange(len(y)), y , c=c , ls=ls)

        pl.title('%i prices from class %i/%i' %(N , i+1 , len(np.unique(lbls))))

    pl.show()

if __name__ == '__main__':
    prices, tickers = dp.loaddata()
    prices = dp.normalization(prices)

    af = AffinityPropagation( preference=-50).fit(prices)
    plot_eachclass(prices, af)




