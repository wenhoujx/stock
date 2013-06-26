import numpy as np 
import utils.data_processing as dp
import Pycluster as pycl
import itertools as it
import pylab as pl

def plot_eachclass(prices, centerid, method='a', dist='e'): 
    k = len(np.unique(centerid))
    colors = it.cycle( 'bgrcmykw') 
    linestyles = it.cycle('_-:') 

    for i in range(k): 
        p = prices[ np.where( centerid == i)]
        N = 30
        if N > p.shape[0]:
            N = p.shape[0]
        pr = p[np.random.randint(0 , p.shape[0], N)]

        pl.figure(i)
        for y, c, ls in zip(pr , colors, linestyles):
            pl.plot( xrange(len(y)), y , c=c, ls=ls) 

        pl.title( 'plot %i of %i prices for class %i / %i' %( N,p.shape[0], i+1 , k))
        pl.savefig( 'figs/plot %i of %i prices for class %i of %i method %s dist %s.png' %( N, p.shape[0], i+1 , k, method, dist))

    pl.show()

def clustering( prices, nclusters, npass, method, dist):
    centerid = pycl.kcluster(prices, nclusters=nclusters,npass=npass, method=method, dist=dist)
    return centerid
    

if __name__ == '__main__':
    prices , tickers = dp.loaddata()
    prices  = dp.normalization( prices) 
    
    # method: 
    #     a : arithmetic mean 
    #     m: median
    # dist:
    #     c: correlation 
    #     a: abs value of correlation 
    #     u: uncentered correlation
    #     x: abs uncentered correlation
    #     s: Spearman's rank correlation
    #     k: Kendall's tau 
    #     e: eculiden distance.
    #     b: city-block distance.
    
    method = 'a'
    dist='k'
    centerid = clustering( prices, nclusters =10 , npass=5, method=method, dist=dist)

    plot_eachclass( prices, centerid[0], method=method, dist=dist)


