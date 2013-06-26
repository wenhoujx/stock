import utils.data_processing as dp 
import numpy as np 
import pylab as pl
import itertools as it
import scipy as sp
from sklearn.cluster import Ward

def plot_eachclass_hie( prices, lbls) :
    # for each label
    for i in range(len(np.unique(lbls))):
        # these prices belong to one class
        p = prices[np.where(lbls == i)]

        # pick at most 100 to plot
        N = 100
        if N > len(p):
            N = len(p) %100
        p = p[np.random.randint( 0 , len(p), N)]
        
        pl.figure(i)
        for y, c, ls in zip( p , it.cycle('bgrcmykw') , it.cycle('_-:')):
            pl.plot(xrange(len(y)) , y , c=c, ls=ls)
        pl.title( '%i prices from class %i / %i' %( N , i+1 , len(np.unique(lbls))))        
        pl.savefig('figs/hie_%i.png' %i) 
    pl.show()

if __name__ == '__main__':
    # first thing is always to load data
    prices, tickers = dp.loaddata()
    prices = dp.normalization( prices )

    # compute the Ward minimum hierarchical clustering
    print ' computing for the hierarchical clustering....'
    ward = Ward( n_clusters = 10).fit(prices)

    # let me plot
    plot_eachclass_hie( prices, ward.labels_)

     


    


