import numpy as np 
import utils.data_processing as dp
import Pycluster as pycl
import itertools as it
import pylab as pl

def plot_eachclass(prices, clusterid, method='a', dist='e'): 
    k = len(np.unique(clusterid))
    colors = it.cycle( 'bgrcmykw') 
    linestyles = it.cycle('_-:') 

    for i in range(k): 
        p = prices[ np.where(clusterid == np.unique(clusterid)[i])]
        N = 30
        if N > p.shape[0]:
            N = p.shape[0]
        pr = p[np.random.randint(0 , p.shape[0], N)]

        pl.figure(i)
        for y, c, ls in zip(pr , colors, linestyles):
            pl.plot( xrange(len(y)), y , c=c, ls=ls) 

        pl.title( 'plot %i of %i prices for class %i / %i' %( N,p.shape[0], i+1 , k))
        pl.savefig( 'figs_tree/tree_%s_%s_plot %i of %i prices for class %i of %i.png' %(method, dist, N, p.shape[0], i+1 , k ))

    pl.show()

def compute_R_tau( prices) :
    with open('spearman_dist.param', 'w') as f: 
        np.save(f, pycl.distancematrix(prices, dist='s'))
    with open('kendal_tau_dist.param', 'w') as f: 
        np.save(f, pycl.distancematrix(prices, dist='k'))


if __name__ == '__main__':
    prices , tickers = dp.loaddata()
    prices  = dp.normalization( prices) 
    
    # method: 
        # s: pairwise single linkage clustering
        # m: pairwise max/complete linkage 
        # c: pairwise centroid linkage 
            # note this cannot be used if distancematrix is provided as an arg.
        # a: piarwise average linkage
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
    # compute_R_tau(prices)
    with open ( 'spearman_dist.param', 'r') as f: 
        s_dist = np.load(f)
    with open ( 'kendal_tau_dist.param', 'r') as f: 
        k_dist = np.load(f)

    if dist =='s':
        tree = pycl.treecluster(distancematrix=s_dist.tolist(), method=method )    
    if dist == 'k':
        tree = pycl.treecluster(distancematrix=k_dist.tolist(), method=method )    

    clusterid = tree.cut(10)
    plot_eachclass( prices, clusterid, method=method, dist=dist)


