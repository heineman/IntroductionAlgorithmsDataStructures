"""
    Demonstrate use of Skip List and some timing

N	SL-RND	AVL-RND	SL-ASC	AVL-ASC	SL-DESC	AVL-DESC
16	0.099	0.071	0.087	0.080	0.090	0.078
32	0.220	0.187	0.180	0.195	0.194	0.196
64	0.490	0.450	0.419	0.480	0.437	0.603
128	1.008	1.262	0.817	1.385	1.048	1.306
256	2.618	2.416	1.700	2.516	2.022	2.392
512	4.938	5.235	3.445	5.529	4.157	5.420
1024	11.139	11.976	7.224	12.310	9.108	12.224
2048	23.865	26.733	15.213	27.141	19.539	27.045
4096	51.796	59.731	32.106	59.661	42.402	59.012
8192	108.350	126.034	65.042	125.523	87.130	131.004
16384	241.471	275.437	136.906	270.313	185.904	270.226
32768	503.276	602.992	285.147	583.087	393.711	580.954
    
    Author: George Heineman
"""
from pyskiplist import SkipList
import random
import unittest
import timeit

from avl import BinaryTree



class SkipListTest(unittest.TestCase):
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

def constructSL(aList):
    """Create SkipList from random sample."""
    sl = SkipList()
    for val in aList:
        sl.insert(val,val)
    return sl

def constructAVL(aList):
    bt = BinaryTree()
    for val in aList:
        bt.add(val)
    return bt

def search(avl, aList):
    """Search through structure (either SL or AVL) and return how many elements from aList are found."""
    ct = 0
    for v in aList:
        if v in avl:
            ct += 1
    return ct

def outputPerformanceTiming():
    """
    Generate Timing with random samples for both construction
    """
    print ('N\tSL-RND\tAVL-RND')
    for trial in [2**_ for _ in range(4,16)]:
        build = f'[random.randint(0, 2 ** 12) for _ in range({trial})]'
        targets = f'[random.randint(0, 2 ** 12) for _ in range({trial})]'
        averages = {}
        structures = ['constructSL', 'constructAVL']    
        for s in structures:
            averages[s] = timeit.timeit(stmt=f'search(structure, targets)', number=1000,
                        setup=f'import random\nfrom __main__ import {s},search\nrandom.seed({trial})\ntargets={targets}\nstructure = {s}({build})')
            averages[s] /= trial

        results = '\t'.join(f'{averages[s]:.4f}' for s in structures)
                       
        print (f'{trial}\t{results}')

def outputConstructionTiming():
    """
    Generate Timing with random samples for both construction
    """
    print ('N\tSL-RND\tAVL-RND\tSL-ASC\tAVL-ASC\tSL-DESC\tAVL-DESC')
    for trial in [2**_ for _ in range(4,16)]:
        numbers = f'random.sample(range({trial}),{trial})'
     
        methods = ['constructSL', 'constructAVL']
        counts = {}
        ascending = {}
        descending = {}
            
        for meth in methods:
            counts[meth] = timeit.timeit(stmt=f'{meth}(numbers)', number=1000,
                        setup=f'import random\nfrom __main__ import {meth}\nrandom.seed({trial})\nnumbers = {numbers}')
            ascending[meth] = timeit.timeit(stmt=f'{meth}(numbers)', number=1000,
                        setup=f'import random\nfrom __main__ import {meth}\nrandom.seed({trial})\nnumbers = list(range({trial}))')
            descending[meth] = timeit.timeit(stmt=f'{meth}(numbers)', number=1000,
                        setup=f'import random\nfrom __main__ import {meth}\nrandom.seed({trial})\nnumbers = list(reversed(range({trial})))')

        results1 = '\t'.join(f'{counts[meth]:.3f}' for meth in methods)
        results2 = '\t'.join(f'{ascending[meth]:.3f}' for meth in methods)
        results3 = '\t'.join(f'{descending[meth]:.3f}' for meth in methods)
                       
        print (f'{trial}\t{results1}\t{results2}\t{results3}')

if __name__ == '__main__':
    print ("Average Performance Times")
    outputPerformanceTiming()
    print ()
    print ("Construction Times")
    outputConstructionTiming()
    
