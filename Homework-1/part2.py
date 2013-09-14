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
    vol            = 0
    daily_ret      = 0
    sharpe         = 0
    cum_ret        = 0    
    dt_timeofday   = dt.timedelta(hours=16) # We need closing prices so the timestamp should be hours=16.
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday) # Get a list of trading days between the start and the end.
    c_dataobj      = da.DataAccess('Yahoo') # Creating an object of the dataaccess class with Yahoo as the source.
    ls_keys        = ['open', 'high', 'low', 'close', 'volume', 'actual_close'] # Keys to be read from the data, it is good to read everything in one go.
    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data   = dict(zip(ls_keys, ldf_data))
    # Filling the data for NAN
    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method='ffill')
        d_data[s_key] = d_data[s_key].fillna(method='bfill')
        d_data[s_key] = d_data[s_key].fillna(1.0)
    # Getting the numpy ndarray of close prices.
    df_rets = d_data['close'].copy() 
    df_rets = df_rets.fillna(method='ffill') 
    df_rets = df_rets.fillna(method='bfill') 
    df_rets = df_rets.fillna(1.0)
    na_rets = df_rets.values
    print("original stock values") 
    print(df_rets['GOOG'])
    
    # print np.std([[0,0], [1,1]])
    
    return vol, daily_ret, sharpe, cum_ret

def main():
    ''' Main Function'''

    dt_start = dt.datetime(2006, 1, 1)
    dt_end   = dt.datetime(2010, 12, 31)
    print "start ", dt_start, " end ", dt_end
    vol, daily_ret, sharpe, cum_ret = simulate(dt_start, dt_end, ['GOOG','AAPL','GLD','XOM'], [0.2,0.3,0.4,0.1])

    print "result ", vol, daily_ret, sharpe, cum_ret

if __name__ == '__main__':
    main()
