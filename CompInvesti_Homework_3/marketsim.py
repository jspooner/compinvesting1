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




if __name__ == '__main__':
    print "start marketsim"
    # cash       = sys.argv[1]
    # orders_csv = sys.argv[2]
    # values_csv = sys.argv[3]
    cash       = 1000000
    orders_csv = '/Users/jspooner/QSTK/Examples/CompInvesti_Homework_3/orders.csv'
    values_csv = "values.csv"

    # orders = np.loadtxt(orders_csv, dtype='S5,f4', delimiter=',', comments="#", skiprows=0)
    # print orders[0]
    orders = pd.read_csv(orders_csv, parse_dates={'date' : [0,1,2]}, skiprows=0, header=None )
    print orders
    
    

    