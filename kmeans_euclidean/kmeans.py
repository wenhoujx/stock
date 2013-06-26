import itertools as it 
import utils.data_processing as data_processing
import numpy as np 
import pylab as pl 

from sklearn import metrics
from sklearn.cluster import KMeans

def kmeans(prices, k ):
    '''
    this function returns the k_means object
    '''
    k_means = KMeans( init = 'k-means++' , n_clusters=k , n_init=10)
    k_means.fit(prices)
    return k_means

def plot_eachclass( prices, k_means): 
    # cycle through colors and lines 
    colors = it.cycle('bgrcmykw')
    linestyles = it.cycle('-:_')
    # number of random prices plot
    Nmin = np.bincount(k_means.labels_).min()
    N = 30
    if (N > Nmin):
        N = Nmin

    # for each class
    for i in range(k_means.cluster_centers_.shape[0]):
        # indices of each class
        idx = np.where(k_means.labels_ == i)
        p = prices[idx]
        center = k_means.cluster_centers_[i]

        pl.figure(i)
        # x axis
        x = xrange(prices.shape[1])
        # randomly pick N 
        randidx = np.random.randint( 0, p.shape[0], N)

        for y , c , ls  in zip( p[randidx], colors, linestyles):
            pl.plot(x, y, c=c , ls=ls)
        pl.plot(x, center, 'r' ,linewidth = 10, label='center line')
        pl.title('random plot 10 prices of class %i / %i' %( i+1, k_means.cluster_centers_.shape[0]))
        pl.legend()
        # save
        pl.savefig('figs/class_%i.png' %(i+1))

    pl.show()
        


if __name__ == '__main__':
    prices, labels = data_processing.loaddata()
    prices =  data_processing.normalization(prices)

    k = 10
    k_means = kmeans(prices, k )

    plot_eachclass(prices, k_means) 
    


