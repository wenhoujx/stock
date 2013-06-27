import numpy as np

def load_R_tau():
    with open ( 'spearman_dist.param', 'r') as f: 
        s_dist = np.load(f)
    with open ( 'kendal_tau_dist.param', 'r') as f: 
        k_dist = np.load(f)

    return s_dist, k_dist
    
