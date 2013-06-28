def compute_R_tau( prices) :
    with open('spearman_dist.param', 'w') as f: 
        np.save(f, pycl.distancematrix(prices, dist='s'))
    with open('kendal_tau_dist.param', 'w') as f: 
        np.save(f, pycl.distancematrix(prices, dist='k'))
