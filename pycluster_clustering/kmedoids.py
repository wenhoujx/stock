from collections import Counter
import matplotlib.pyplot as plt
import numpy as np 
import utils.data_processing as dp
from utils.load_R_tau import load_R_tau
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
    for iter_count, (i, _) in enumerate(Counter(centerid).most_common()):
        pr_class_i = prices[ np.where(centerid == i)]
        N = 30
        if N > pr_class_i.shape[0]:
            N = pr_class_i.shape[0]
        prN = pr_class_i[np.random.randint(0,pr_class_i.shape[0], N)] 
        plt.subplot(3,3,iter_count+1)
        for y, c, ls in zip(prN, colors, linestyles):
            plt.plot(xrange(len(y)),  y, c=c, ls=ls)
        plt.title( '%i of %i plotted' %(N, pr_class_i.shape[0]))
    plt.tight_layout()
    plt.savefig(folderpath)
    plt.show()


if __name__ == '__main__':
    prices , tickers = dp.loaddata()
    prices  = dp.normalization( prices) 

    sdist, kdist = load_R_tau()

    nclusters = 9
    npass = 50
    for dist in ['e', 's', 'k']:
        if dist == 'e':
            edist = pycl.distancematrix(prices, dist=dist)
            centerid  = pycl.kmedoids(distance=edist, nclusters=nclusters, npass=npass)
            plot_eachclass( prices, centerid[0], folderpath='figs_kmedoids/euclidean.png')
        elif dist == 's':
            centerid = pycl.kmedoids(distance=sdist.tolist(), nclusters=nclusters, npass=npass)
            plot_eachclass( prices, centerid[0], folderpath='figs_kmedoids/spearman.png')
        else:
            centerid = pycl.kmedoids(distance=kdist.tolist(), nclusters=nclusters, npass=npass)
            plot_eachclass( prices, centerid[0], folderpath='figs_kmedoids/kendall.png')
