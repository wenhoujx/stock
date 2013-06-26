import numpy as np 
import itertools as it 
import pylab as pl 

def loaddata(): 
    prices , labels = (np.load('../data/valid_prices') , np.load('../data/valid_labels'))
    prices = prices.astype(np.float)
    # delete rows with all zeros
    prices = prices[ ~ np.all( prices==0, axis=1)]
    return prices , labels

def rand_plot(  prices ,labels, saveas ,N = 10) : 
    M, dim = prices.shape
    idx = np.random.randint( 0 , M, N) 
    colors = it.cycle( 'bgrcmykw') 
    
    x = xrange( dim)
    pl.figure()

    for price, lbl, c  in zip ( prices[idx] , labels[idx], colors):
        pl.plot(x, price, c=c ,label=lbl)
    
    pl.title('random plot %i stock prices' %N)
    # pl.legend() 
    pl.xlabel('day1 to day256') 
    pl.ylabel('price in dolloar')
    pl.show() 
    # pl.savefig(saveas)

def normalization(prices):
    # prices /= prices.max(axis=1)[:, None]
    # norm = 1 
    prices /= np.apply_along_axis( np.linalg.norm, axis = 1 , arr = prices)[:,None]
    return prices
    
    
if __name__ == '__main__': 
    prices, labels = loaddata()
    prices = prices.astype(np.float)
    N = 10
    rand_plot( prices, labels , N = N, saveas ='random_display_before_normalization' )
    prices = normalization( prices)
    rand_plot(prices, labels, N=N, saveas = 'random_display_after_normalization.png')
