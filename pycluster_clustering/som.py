from collections import Counter
import matplotlib.pyplot as plt
import numpy as np 
import utils.data_processing as dp
import Pycluster as pycl

import itertools as it
def plot_eachclass( prices, clusterid, folderpath):
    '''
    # dist:
    #     c: correlation 
    #     a: abs value of correlation 
    #     u: uncentered correlation
    #     x: abs uncentered correlation
    #     s: Spearman's rank correlation
    #     k: Kendall's tau 
    #     e: eculiden distance.
    #     b: city-block distance.
    '''

    colors = it.cycle('bgrcmykw')
    linestyles = it.cycle('-:_')
    cid = clusterid[:,0]*10+clusterid[:,1]

    plt.figure()
    # plot the most frequent ones first
    for iter_counter, ( i, _) in enumerate( Counter(cid).most_common()):
        pr_class_i = prices[np.where(cid ==i )]
        if pr_class_i.shape[0] == 0: 
            continue
        # plot at most 30 prices for each class
        N = 30
        if N > pr_class_i.shape[0]:
            N = pr_class_i.shape[0]
        prN = pr_class_i[np.random.randint(0,pr_class_i.shape[0], N)] 
        plt.subplot(3,3,iter_counter)
        for y, c, ls in zip(prN, colors, linestyles):
            plt.plot(xrange(len(y)),  y, c=c, ls=ls)
        plt.title( '%i of %i plotted' %(N, pr_class_i.shape[0]))
    # make sure the titles and xaxis don't overlap
    plt.tight_layout()
    plt.savefig(folderpath, dpi=200)
    plt.show()


if __name__ == '__main__':
    prices , tickers = dp.loaddata()
    prices  = dp.normalization( prices) 


    for dist in [ 'e', 's', 'k', 'b']:
        if dist == 'e':
            print 'computing euclidean clustering'
            clusterid , _ = pycl.somcluster(prices, nxgrid=3, nygrid=3, dist=dist)
            plot_eachclass( prices, clusterid, folderpath='figs_som/euclidean.png')
        elif dist == 's':
            print 'computing spearman clustering'
            clusterid , _ = pycl.somcluster(prices, nxgrid=3, nygrid=3, dist=dist)
            plot_eachclass( prices, clusterid, folderpath='figs_som/spearman.png')
        elif dist=='k':
            print 'computing kendall clustering'
            clusterid , _ = pycl.somcluster(prices, nxgrid=3, nygrid=3, dist=dist)
            plot_eachclass( prices, clusterid, folderpath='figs_som/kendall.png')
        elif dist=='b':
            print 'computing city block clustering'
            clusterid, _ = pycl.somcluster( prices, nxgrid=3, nygrid=3, dist=dist)
            plot_eachclass(prices, clusterid, folderpath='figs_som/cityblock.png')
