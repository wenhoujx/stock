from collections import Counter
import matplotlib.pyplot as plt
import numpy as np 
import utils.data_processing as dp
import Pycluster as pycl

import itertools as it
def plot_eachclass( prices, centerid, folderpath):
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

    plt.figure()
    # plot the most frequent ones first
    for iter_count, (i, _) in enumerate(Counter(centerid).most_common()):
        pr_class_i = prices[ np.where(centerid == i)]
        # plot at most 30 prices for each class
        N = 30
        if N > pr_class_i.shape[0]:
            N = pr_class_i.shape[0]
        prN = pr_class_i[np.random.randint(0,pr_class_i.shape[0], N)] 
        plt.subplot(3,3,iter_count+1)
        for y, c, ls in zip(prN, colors, linestyles):
            plt.plot(xrange(len(y)),  y, c=c, ls=ls)
        plt.title( '%i of %i plotted' %(N, pr_class_i.shape[0]))
    # make sure the titles and xaxis don't overlap
    plt.tight_layout()
    plt.savefig(folderpath, dpi=200)
    # plt.show()


if __name__ == '__main__':
    prices , tickers = dp.loaddata()
    prices  = dp.normalization( prices) 

    nclusters = 9
    npass = 50
    for dist in [ 'k']:
        if dist == 'e':
            print 'computing euclidean clustering'
            centerid  = pycl.kcluster(prices, nclusters = nclusters, npass = npass, dist=dist)
            plot_eachclass( prices, centerid[0], folderpath='figs_kmeans/euclidean.png')
        elif dist == 's':
            print 'computing spearman R clustering'
            centerid = pycl.kcluster( data=prices, nclusters=nclusters, npass=npass, dist=dist)
            plot_eachclass( prices, centerid[0], folderpath='figs_kmeans/spearman.png')
        else:
            print 'computing kendall tau clustering'
            centerid = pycl.kcluster( data=prices, nclusters=nclusters, npass=20, dist=dist)
            plot_eachclass( prices, centerid[0], folderpath='figs_kmeans/kendall.png')
