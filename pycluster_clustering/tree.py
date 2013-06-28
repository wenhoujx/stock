from collections import Counter
import numpy as np 
import utils.data_processing as dp
import Pycluster as pycl
import itertools as it
import matplotlib.pyplot as plt

def plot_eachclass(prices, clusterid, folderpath): 
    colors = it.cycle( 'bgrcmykw') 
    linestyles = it.cycle('_-:') 

    plt.figure()
    for iter_count, (i, _) in enumerate(Counter(clusterid).most_common()):
        pr_class_i = prices[ np.where(clusterid == i)]
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
    plt.show()

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
    with open ( 'spearman_dist.param', 'r') as f: 
        s_dist = np.load(f)
    with open ( 'kendal_tau_dist.param', 'r') as f: 
        k_dist = np.load(f)

    for method in ['s', 'm', 'a']: 
        for dist in ['e', 's','k','b']:
            if method == 's': 
                methodstring = 'minLinkage_'
            elif method == 'm': 
                methodstring = 'maxLinkage_'
            elif method =='a': 
                methodstring = 'averageLinkage_'

            if dist == 'e':
                print methodstring + 'euclidean clustering'
                tree = pycl.treecluster(data=prices, method=method, dist=dist)
                folderpath = 'figs_tree/' + methodstring + 'euclidean.png'
            elif dist == 's': 
                print methodstring + 'spearman clustering'
                tree = pycl.treecluster(distancematrix=s_dist.tolist(), method=method )    
                folderpath = 'figs_tree/' + methodstring + 'spearman.png'
            elif dist == 'k':
                print methodstring + 'kendall clustering'
                tree = pycl.treecluster(distancematrix=k_dist.tolist(), method=method )    
                folderpath = 'figs_tree/' + methodstring + 'kendall.png'
            elif dist =='b': 
                print methodstring + 'city block clustering'
                tree = pycl.treecluster(data=prices, method=method, dist=dist)
                folderpath = 'figs_tree/' + methodstring + 'city_block.png'

            nclusters = 9
            clusterid = tree.cut(nclusters)
            plot_eachclass( prices, clusterid, folderpath)


