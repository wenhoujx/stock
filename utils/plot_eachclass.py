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

    for i in range(len(np.unique(centerid))):
        pr_class_i = prices[ np.where(centerid == np.unique(centerid)[i])]
        N = 30
        if N > pr_class_i.shape[0]:
            N = pr_class_i.shape[0]
        prN = pr_class_i[np.random.randint(0,pr_class_i.shape[0], N)] 
        pl.subplot(3,3,i+1)
        for y, c, ls in zip(prN, colors, linestyles):
            pl.plot(xrange(len(y)),  y, c=c, ls=ls)
        pl.title( '%i of %i in the clusters plotted' %(N, pr_class_i.shape[0]))
    # pl.tight_layout()
    pl.show()

