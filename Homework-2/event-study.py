#!/usr/local/bin/python
'''
http://wiki.quantsoftware.org/index.php?title=CompInvestI_Homework_2
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
    true
    
    
    
    
if __name__ == '__main__':
    print "start"
    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))