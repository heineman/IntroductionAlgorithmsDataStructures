"""
    Demonstrate a number of simple algorithms to define the terminology
    used to characterize algorithm performance and space usage.
    
    Author: George Heineman
"""
import random
import timeit
import unittest

def contains(aList, tgt):
    """
    Use built-in 'in' operation as implementation.
    """
    return tgt in aList

def sortedContains(aList, tgt):
    """
    Since aList is sorted, stop once element is larger than 'target'.
    """
    for v in aList:
        if v > tgt:
            return False
        if v == tgt:
            return True
    return False

def binaryArraySearch(aList, tgt):
    """
    Return True if aList contains tgt, False otherwise. 
    """
    lo = 0
    hi = len(aList) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if tgt < aList[mid]:
            hi = mid - 1
        elif tgt > aList[mid]:
            lo = mid + 1
        else:
            return True
    return False

class TimingContainsTest(unittest.TestCase):
    """
    Unit test cases to briefly validate methods.
    """
    def setUp(self):
        theList = [random.randint(0, 2 ** 24) for _ in range(512)]
        self.numbers = sorted(theList)
        self.target = self.numbers[-1]
        
    def testCheckContains(self):
        self.assertTrue(contains(self.numbers, self.target))
        self.assertFalse(contains(self.numbers, -1))

    def testCheckSortedContains(self):
        self.assertTrue(sortedContains(self.numbers, self.target))
        self.assertFalse(sortedContains(self.numbers, -1))

    def testCheckBinaryArraySearch(self):
        self.assertTrue(binaryArraySearch(self.numbers, self.target))
        self.assertFalse(binaryArraySearch(self.numbers, -1))
        

def outputTiming():
    """
    Generate timing report using random integers from 0 to 16777216,
    which greatly reduces the chance that a duplicate exists, thus
    ensuring the worst case scenario. Use random.seed(trial) to try
    to produce identical number sets across different approaches.
    """
    print ('N\tContains\tSortContains\tBinaryArraySearch')
    for trial in [2**_ for _ in range(1,16)]:
        numbers = f'sorted([random.randint(0, 2 ** 24) for _ in range({trial})])'
     
        methods = ['contains', 'sortedContains', 'binaryArraySearch']
        counts = {}
        for meth in methods:
            counts[meth] = timeit.timeit(stmt=f'{meth}(numbers, numbers[-1])', number=10000,
                        setup=f'import random\nfrom __main__ import {meth}\nrandom.seed({trial})\nnumbers = {numbers}')

        results = '\t'.join(f'{counts[meth]:f}' for meth in methods)
        print (f'{trial}\t{results}')

if __name__ == '__main__':
    outputTiming()
    unittest.main()
    



