import numpy as np 
import utilfuns.data_processing as dp
import Pycluster as pycl
import utilfuns.plot_eachclass as pe 
# import plotclusters as pe 

if __name__ == '__main__':
    prices , tickers = dp.loaddata()
    prices  = dp.normalization( prices) 
    
    nclusters = 9
    npass = 50
    for dist in [ 'e', 's', 'k']:
        if dist == 'e':
            print 'computing euclidean clustering'
            centerid  = pycl.kcluster(prices, nclusters = nclusters, npass = npass, dist=dist)
            pe.plot_eachclass( prices, centerid[0], folderpath='figs_kmeans/euclidean.png')
        elif dist == 's':
            print 'computing spearman R clustering'
            centerid = pycl.kcluster( data=prices, nclusters=nclusters, npass=npass, dist=dist)
            pe.plot_eachclass( prices, centerid[0], folderpath='figs_kmeans/spearman.png')
        else:
            print 'computing kendall tau clustering'
            centerid = pycl.kcluster( data=prices, nclusters=nclusters, npass=20, dist=dist)
            pe.plot_eachclass( prices, centerid[0], folderpath='figs_kmeans/kendall.png')

