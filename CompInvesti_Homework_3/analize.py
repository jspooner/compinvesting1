#!/usr/local/bin/python
'''
python analyze.py values.csv $SPX

Part 2: Create a portfolio analysis tool, analyze.py, that takes a command line like this:

The tool should read in the daily values (cumulative portfolio value) from values.csv and plot them. 
It should use the symbol on the command line as a benchmark for comparison (in this case $SPX). 
Using this information, analyze.py should:

'''

import sys

if __name__ == '__main__':
    print "start analize"
    print 'Argument List:', str(sys.argv)