"""
    Demonstrate a number of simple algorithms to define the terminology
    used to characterize algorithm performance and space usage.

    Demonstrate O(n) behavior with O(n) storage for determining whether
    list of positive integers contains duplicate values.
    
    Shows alternate implementation with O(n^2) behavior with O(1) storage
    to solve same problem

    Shows alternative implementation with O(n) behavior and O(n) storage
    to solve same problem
    
    Author: George Heineman
"""
import random
import timeit
import unittest

def sumValues(aList):
    """
    Return the sum of the values in the list.
    """
    sum = 0
    for d in aList:
        sum += d
    return sum

def uniqueCheckSet(aList):
    """
    Return True if aList contains any duplicates. Its contents are not
    altered and completes in O(n) time with O(n) space required. The
    individual elements must be hashable.
    """
    check = set()
    for v in aList:
        if v in check:
            return True
        check.add(v)
    return False

def uniqueCheckLoop(aList):
    """
    Return True if aList contains any duplicates. Its contents are not
    altered and completes in O(n^2) time with no space required. 
    """
    n = len(aList)
    for i in range(n-1):
        for j in range(i+1, n):
            if aList[i] == aList[j]:
                return True
    return False

def uniqueCheckString(aList):
    """
    Return True if aList contains any duplicates. Its contents are not
    altered. A single string is constructed of the form ",13,245,18," which
    contains three values seen so far (i.e., 13, 245 and 18) in comma-separated form.
    """
    check = ','
    for v in aList:
        if f',{v},' in check:
            return True
        check = f'{check}{v},'
    return False

class TimingTest(unittest.TestCase):
    """
    Unit test cases to briefly validate methods.
    """
    def setUp(self):
        noDuplicate = [random.randint(0, 2 ** 24) for _ in range(512)]
        withDuplicate = list(noDuplicate) + [noDuplicate[len(noDuplicate)//2]]
        self.numbers = noDuplicate
        self.numbersWithDuplicate = withDuplicate
        
    def testCheckFast(self):
        self.assertTrue(uniqueCheckSet(self.numbersWithDuplicate))
        self.assertFalse(uniqueCheckSet(self.numbers))

    def testCheckSlow(self):
        self.assertTrue(uniqueCheckString(self.numbersWithDuplicate))
        self.assertFalse(uniqueCheckString(self.numbers))

    def testCheckSlowest(self):
        self.assertTrue(uniqueCheckLoop(self.numbersWithDuplicate))
        self.assertFalse(uniqueCheckLoop(self.numbers))

def outputTiming():
    """
    Generate timing report using random integers from 0 to 16777216,
    which greatly reduces the chance that a duplicate exists, thus
    ensuring the worst case scenario. Use random.seed(trial) to try
    to produce identical number sets across different approaches.
    """
    print ('N\tSum     \tSet\t        String\t        Loop')
    for trial in [2**_ for _ in range(1,11)]:
        numbers = f'[random.randint(0, 2 ** 24) for _ in range({trial})]'
     
        methods = ['sumValues', 'uniqueCheckSet', 'uniqueCheckString', 'uniqueCheckLoop' ]
        counts = {}
        for meth in methods:
            counts[meth] = timeit.timeit(stmt=f'{meth}(numbers)', number=1000,
                        setup=f'import random\nfrom __main__ import {meth}\nrandom.seed({trial})\nnumbers = {numbers}')

        results = '\t'.join(f'{counts[meth]:f}' for meth in methods)
        print (f'{trial}\t{results}')

if __name__ == '__main__':
    outputTiming()
    unittest.main()
    



