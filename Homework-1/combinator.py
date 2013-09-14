#!/usr/local/bin/python

import numpy as np

def createCombinations(items, minValue = 0.0, maxValue = 1.0, increment=0.10):
    
    steps = int((maxValue - minValue) / increment) + 1
    # print 'we will take ' + `steps` + ' steps'

    combinationTotal = steps**items
    # print 'there are ' + `combinationTotal` + 'combinations'
        
    combinationList = np.empty((combinationTotal,items))
    combinationList.fill(minValue)
    
    values = range(items)
    cycles = range(items)
    for i in values:
        values[i] = 0
        cycles[i] = 0

    # print values
    # print combinationList

    for r in range(combinationTotal):
                
        for c in range(items):
            
            if(values[c] > maxValue):
                values[c] = minValue
                cycles[c] += 1         

                if(values[c] < len(values)-1):
                    values[c + 1] += increment   

            combinationList[r,c] = values[c]

            if(c == 0):
                values[c] += increment


        # print r
        # print combinationList[r,:]
    
    return combinationList

def calcPossibleAllocations(items, minValue = 0.0, maxValue = 1.0, increment=0.10):
    
    combos = createCombinations(items, minValue, maxValue, increment)
    shape = combos.shape
    
    comboSum = np.sum(combos, axis=1)
    # np.sum results are not exactly 1, they are 1.000...0001
    comboSum = np.matrix.round(comboSum, 15)    

    combos = combos[comboSum == 1]
    shape = combos.shape

    # for i in range(shape[0]):
    #     print combos[i,:]

    return combos

def main():
    print calcPossibleAllocations(4)

if __name__ == '__main__':
    main()