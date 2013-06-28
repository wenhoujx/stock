import Pycluster as pycl 
import numpy as np

def computeR( prices, filename='spearman_dist.param'):
    with open ( filename,'w') as f:
        np.save( f, pycl.distancematrix(prices,dist='s'))

def compute_tau( prices, filename='kendall_dist.param'):
    with open ( filename,'w') as f:
        np.save( f, pycl.distancematrix(prices,dist='s'))

def compute_R_tau(prices):
    print 'computing kendall tau'
    compute_tau(prices) 
    print 'computing spearman R'
    compute_R(prices)

