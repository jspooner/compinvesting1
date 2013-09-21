#!/usr/local/bin/python
'''
http://wiki.quantsoftware.org/index.php?title=CompInvestI_Homework_2

Part 2: Create an event study profile of a specific "known" event on S&P 500 stocks, and compare its 
impact on two groups of stocks.

The event is defined as when the actual close of the stock price drops below $5.00, more specifically, when:

price[t-1] >= 5.0
price[t] < 5.0
an event has occurred on date t. Note that just because the price is below 5 it is not an event for every day 
that it is below 5, only on the day it first drops below 5.

Evaluate this event for the time period January 1, 2008 to December 31, 2009. Compare the results using two 
lists of S&P 500 stocks: A) The stocks that were in the S&P 500 in 2008 (sp5002008.txt), and B) the stocks that 
were in the S&P 500 in 2012 (sp5002012.txt). These equity lists are in the directory QSData/Yahoo/Lists
'''

import pandas as pd
import numpy as np
import math
import copy
import QSTK.qstkutil.qsdateutil as du
import datetime as dt
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkstudy.EventProfiler as ep

def find_events(ls_symbols, d_data):
    '''Finding the events dataframe'''
    df_actual_close  = d_data['actual_close']
    ts_market = df_actual_close['SPY']
    
    print "Finding Events"
    
    # Creating an empty dataframe
    df_events = copy.deepcopy(df_actual_close)
    df_events = df_events * np.NAN
    
    # Time stamps for the event range
    ldt_timestamps = df_actual_close.index
    
    for s_sym in ls_symbols:
        print('.'),
        for i in range(1, len(ldt_timestamps)):
            # Calculate the returns for this day
            f_symprice_today = df_actual_close[s_sym].ix[ldt_timestamps[i]]
            f_symprice_yest  = df_actual_close[s_sym].ix[ldt_timestamps[i - 1]]

            if f_symprice_yest >= 10.0 and f_symprice_today < 10.0:
                print "Found event for ", s_sym, " on ", ldt_timestamps[i], " yesterday ", f_symprice_yest, " f_symprice_today ", f_symprice_today
                df_events[s_sym].ix[ldt_timestamps[i]] = 1
    
    return df_events

def do_test_for(dt_start, dt_end, symbol_list):
    """docstring for do_test_for"""
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
    dataobj        = da.DataAccess('Yahoo')
    ls_symbols     = dataobj.get_symbols_from_list(symbol_list)
    ls_symbols.append('SPY')
    
    ls_keys  = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data   = dict(zip(ls_keys, ldf_data))
    
    for s_key in ls_keys:
        d_data[s_key] = d_data[s_key].fillna(method='ffill')
        d_data[s_key] = d_data[s_key].fillna(method='bfill')
        d_data[s_key] = d_data[s_key].fillna(1.0)
    
    df_events = find_events(ls_symbols, d_data)
    study_name = 'EventStudy-10dollarevent-' + symbol_list + 'pdf'
    print "Creating Study", study_name
    ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                s_filename=study_name, b_market_neutral=True, b_errorbars=True,
                s_market_sym='SPY')


if __name__ == '__main__':
    print "start"
    dt_start       = dt.datetime(2008, 1, 1)
    dt_end         = dt.datetime(2009, 12, 31)
    do_test_for(dt_start, dt_end, 'sp5002008')
    # do_test_for(dt_start, dt_end, 'sp5002012')
