import numpy as np 
import utils.data_processing as dp
import Pycluster as pycl
import itertools as it
import pylab as pl

def plot_eachclass(prices, centerid,  dist='e'): 
    k = len(np.unique(centerid))
    colors = it.cycle( 'bgrcmykw') 
    linestyles = it.cycle('_-:') 

    for i in range(k): 
        p = prices[ np.where( centerid == centerid[i])]
        N = 30
        if N > p.shape[0]:
            N = p.shape[0]
        pr = p[np.random.randint(0 , p.shape[0], N)]

        pl.figure(i)
        for y, c, ls in zip(pr , colors, linestyles):
            pl.plot( xrange(len(y)), y , c=c, ls=ls) 

        pl.title( 'plot %i of %i prices for class %i / %i' %( N,p.shape[0], i+1 , k))
        pl.savefig( 'figs_kmeds/plot %i of %i prices for class %i of %i dist %s.png' %( N, p.shape[0], i+1 , k, dist))

    # pl.show()

    

if __name__ == '__main__':
    prices , tickers = dp.loaddata()
    prices  = dp.normalization( prices) 
    
    # dist:
    #     c: correlation 
    #     a: abs value of correlation 
    #     u: uncentered correlation
    #     x: abs uncentered correlation
    #     s: Spearman's rank correlation
    #     k: Kendall's tau 
    #     e: eculiden distance.
    #     b: city-block distance.
    
    dist='k'
    print 'computing distance matrix'
    distance = pycl.distancematrix( prices, dist=dist)
    print 'computing kmedoids clustering'
    centerid = pycl.kmedoids( distance, npass= 1, nclusters=10)
    print 'plotting'
    plot_eachclass( prices, centerid[0],  dist=dist)


