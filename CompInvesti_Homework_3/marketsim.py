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



if __name__ == '__main__':
    print "start marketsim"
    print 'Argument List:', str(sys.argv)
    print sys.argv[1]
    