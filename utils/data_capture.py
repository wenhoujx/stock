import urllib2
import csv
import numpy as np
import ystockquote as ys 

def get_tickers(filename='ticker_symbol.csv'):
    tickers = np.genfromtxt( filename, dtype='|S10')
    # this one line above does everything below:

    # with open(filename, 'rU') as f :
    #     t = csv.reader(f)
    #     # get the first numberoflines ticker symbols
    #     tickers = [t.next() for x in xrange(numberoflines)]
    # 
    # # convert to array
    # tickers = np.array(tickers)

    return tickers

def get_historical_prices(tickers , numberofprices = 20000):
    # this defalut value means fetch all valid data.

    stopdate = '2013-01-01'
    startdate ='2012-01-01'

    # just to make the debug not that boring when go through long tickers_list
    # anything smaller than these much is considered useless, this is 2**8
    dim = 256
    # is there a better way to not write these two lines?
    prices = np.zeros(( 1, dim))
    labels = np.zeros((1,1))
    valid_url = 0

    for ticker in tickers: 
        try: 
            # I only want to get the close data, which is the 4th column
            price = np.array( ys.get_historical_prices(ticker , startdate, stopdate) )[1:,3].transpose() 
            if price.size >=dim: 
                prices = np.vstack((prices, price[:dim]))
                labels = np.vstack((labels, [ticker]))
                valid_url +=1 
                print 'capture %i / %i ' %( valid_url, numberofprices)

                if valid_url >= numberofprices:
                    break

        # some url s are invalid
        except urllib2.URLError: 
            # make everything not so boring
            print 'invalid HTTP address' 
    
    # because the first rows are all zeros
    prices = prices[1:]
    labels = labels[1:]

    # save to files
    with open( 'valid_prices_all', 'w') as f:
        np.save(f, prices)

    with open('valid_labels_all' , 'w') as f:
        np.save(f, labels)

    return prices, labels


if __name__ == '__main__':
    tickers = get_tickers()
    prices, labels = get_historical_prices(tickers )
    
    






