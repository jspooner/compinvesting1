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

def simulate(dt_start, dt_end, equities, allocations):
    '''Simulate Function'''
    vol       = 0
    daily_ret = 0
    sharpe    = 0
    cum_ret   = 0
    # We need closing prices so the timestamp should be hours=16.
    dt_timeofday = dt.timedelta(hours=16)

    # Get a list of trading days between the start and the end.
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
    
    print ldt_timestamps
    
    
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
