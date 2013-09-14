#!/usr/local/bin/python
'''
Part 2
http://wiki.quantsoftware.org/index.php?title=CompInvestI_Homework_1
'''

# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def simulate(dt_start, dt_end, ls_symbols, allocations):
    '''Simulate Function'''
    dt_timeofday   = dt.timedelta(hours=16) # We need closing prices so the timestamp should be hours=16.
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday) # Get a list of trading days between the start and the end.
    c_dataobj      = da.DataAccess('Yahoo') # Creating an object of the dataaccess class with Yahoo as the source.
    ls_keys        = ['open', 'high', 'low', 'close', 'volume', 'actual_close'] # Keys to be read from the data, it is good to read everything in one go.
    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data   = dict(zip(ls_keys, ldf_data))
    # Getting the numpy ndarray of close prices.
    na_price = d_data['close'].values
    print na_price
    print "# Normalizing the prices to start at 1 and see relative returns"
    na_normalized_price = na_price / na_price[0, :]
    print na_normalized_price
    print "# Multiply each column by the allocation to the corresponding equity."
    na_normalized = na_normalized_price.copy()
    na_price_alloc = na_normalized * allocations
    print na_price_alloc
    print "# Sum each row for each day. That's your cumulative daily portfolio value."
    na_portfolio = np.sum(na_price_alloc, axis=1)
    na_port = na_portfolio.copy()
    print na_port
    print "# Copy the normalized prices to a new ndarry to find returns."
    na_ret = tsu.returnize0(na_port)
    print "# Statistics from the total portfolio value."
    daily_return = np.average(na_ret)
    vol          = np.std(na_ret)
    sharpe_ratio = ((252)**(.5))*(daily_return/vol)
    cum_ret      = na_portfolio[len(na_portfolio)-1]
    
    return vol, daily_return, sharpe_ratio, cum_ret

def main():
    ''' Main Function'''

    dt_start    = dt.datetime(2011, 1, 1)
    dt_end      = dt.datetime(2011, 12, 31)
    symbols     = ['AAPL', 'GLD', 'GOOG', 'XOM']
    allocations = [0.4, 0.4, 0.0, 0.2]

    vol, daily_ret, sharpe, cum_ret = simulate(dt_start, dt_end, symbols, allocations)
    print "================="
    print "Start Date:" , dt_start #January 1, 2011
    print "End Date:" , dt_end #December 31, 2011
    print "Symbols: ", symbols
    print "Optimal Allocations:" , allocations #[0.4, 0.4, 0.0, 0.2]
    print "Sharpe Ratio:" , sharpe
    print "Volatility (stdev of daily returns): ", vol
    print "Average Daily Return: ",  daily_ret
    print "Cumulative Return:" ,  cum_ret
    
    
    
    

if __name__ == '__main__':
    main()
