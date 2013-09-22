#!/usr/local/bin/python
'''
python marketsim.py 1000000 orders.csv values.csv

Where the number represents starting cash and orders.csv is a file of orders organized like this:

    Year, Month, Day, Symbol, BUY or SELL, Number of Shares
    2008,    12,   3,   AAPL,         BUY, 130
    2008,    12,   8,   AAPL,        SELL, 130
    2008,    12,   5,    IBM,         BUY, 50

Your simulator should calculate the total value of the portfolio for each day using adjusted closing prices
(cash plus value of equities) and print the result to the file values.csv. The 
contents of the values.csv file should look something like this:

Year, Month, Day, total value of portfolio
2008, 12, 3, 1000000
2008, 12, 4, 1000010
2008, 12, 5, 1000250


'''

import sys
# QSTK Imports
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def get_adjusted_close_for(symbol):
    """docstring for get_adjusted_close_for"""
    pass

if __name__ == '__main__':
    print "start marketsim"
    # cash       = sys.argv[1]
    # orders_csv = sys.argv[2]
    # values_csv = sys.argv[3]
    cash       = 1000000
    orders_csv = '/Users/jspooner/QSTK/Examples/CompInvesti_Homework_3/orders.csv'
    values_csv = "values.csv"
    
    orders = pd.read_csv(orders_csv, parse_dates={'date' : [0,1,2]}, skiprows=0, header=None )
    print orders['date']
    
    dt_timeofday   = dt.timedelta(hours=16) # We need closing prices so the timestamp should be hours=16.
    ldt_timestamps = du.getNYSEdays(orders['date'][0], orders['date'][len(orders['date'])-1], dt_timeofday)
    c_dataobj      = da.DataAccess('Yahoo') # Creating an object of the dataaccess class with Yahoo as the source.
    ls_keys        = ['open', 'high', 'low', 'close', 'volume', 'actual_close'] # Keys to be read from the data, it is good to read everything in one go.
    # Reading the data, now d_data is a dictionary with the keys above.
    # Timestamps and symbols are the ones that were specified before.
    ldf_data = c_dataobj.get_data(ldt_timestamps, orders[3].drop_duplicates().values, ls_keys)
    d_data   = dict(zip(ls_keys, ldf_data))
    
    
    

    