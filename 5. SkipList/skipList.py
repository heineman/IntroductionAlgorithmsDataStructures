"""
    Demonstrate use of Skip List and some timing

Stress Test Performance
N	SL-Stress	AVL-Stress
16	0.0891		0.0989
32	0.0926		0.1013
64	0.0955		0.1071
128	0.1082		0.1153
256	0.1328		0.1347
512	0.1819		0.1783
1024	0.2872		0.2669
2048	0.4979		0.4496
4096	0.9046		0.7969
8192	1.6538		1.4289
16384	3.0994		2.5919
32768	5.6789		4.8394

AVL trees outperform SkipLists on randomized stress tests

Average Performance Times
N           SL-RND      AVL-RND
16          0.0021      0.0007
32          0.0025      0.0008
64          0.0027      0.0008
128         0.0032      0.0010
256         0.0034      0.0011
512         0.0042      0.0012
1024        0.0045      0.0013
2048        0.0047      0.0015
4096        0.0054      0.0016
8192        0.0059      0.0016
16384       0.0065      0.0016
32768       0.0071      0.0016


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

def addToAVL(avl, val):
    """To overcome API mismatch, use this function for adding to AVL."""
    avl.add(val)

def addToSkipList(sl, val):
    """To overcome API mismatch, use this function for adding to SkipList."""
    sl.insert(val,val)

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

def stressTest(collection, adder, numSteps):
    """Stress test (either an AVL or a SkipList)."""
    for _ in range(1000):
        adder(collection, random.randint(0, 2 ** 12))

    # now take turns randomly inserting, or deleting values
    for _ in range(numSteps):
        r = random.randint(0, 2 ** 12)
        if r in collection:
            collection.remove(r)
        else:
            adder(collection, r)
            
    # at end, try to remove whole bunch only
    for _ in range(numSteps):
        r = random.randint(0, 2 ** 12)
        if r in collection:
            collection.remove(r)

def stressTestTiming():
    """
    Generate Timing for both constructions
    """
    print ('N\tSL-Stress\tAVL-Stress')
    for trial in [2**_ for _ in range(4,15)]:
        averages = {}
        structures = [addToSkipList, addToAVL]    
        averages['AVL'] = timeit.timeit(stmt=f'stressTest(BinaryTree(), addToAVL, {trial})', number=10,
                        setup=f'import random\nfrom avl import BinaryTree\nfrom __main__ import stressTest,addToAVL\nrandom.seed({trial})')/10

        averages['SL'] = timeit.timeit(stmt=f'stressTest(SkipList(), addToSkipList, {trial})', number=10,
                        setup=f'import random\nfrom pyskiplist import SkipList\nfrom __main__ import stressTest,addToSkipList\nrandom.seed({trial})')/10

        results = '\t'.join(f'{averages[s]:.4f}' for s in ['SL', 'AVL'])
                       
        print (f'{trial}\t{results}')
     
def outputPerformanceTiming():
    """
    Generate Timing with random samples for both construction
    """
    print ('N\tSL-RND\tAVL-RND')
    for trial in [2**_ for _ in range(4,15)]:
        build = f'[random.randint(0, 2 ** 12) for _ in range({trial})]'
        targets = f'[random.randint(0, 2 ** 12) for _ in range({trial})]'
        trials = {}
        structures = ['constructSL', 'constructAVL']    
        for s in structures:
            trials[s] = timeit.timeit(stmt=f'search(structure, targets)', number=100,
                        setup=f'import random\nfrom __main__ import {s},search\nrandom.seed({trial})\ntargets={targets}\nstructure = {s}({build})')/100
        results = '\t'.join(f'{trials[s]:.4f}' for s in structures)
                       
        print (f'{trial}\t{results}')

def outputConstructionTiming():
    """
    Generate Timing with random samples for both construction
    """
    print ('N\tSL-RND\tAVL-RND\tSL-ASC\tAVL-ASC\tSL-DESC\tAVL-DESC')
    for trial in [2**_ for _ in range(4,15)]:
        numbers = f'random.sample(range({trial}),{trial})'
     
        methods = ['constructSL', 'constructAVL']
        counts = {}
        ascending = {}
            
        for meth in methods:
            counts[meth] = timeit.timeit(stmt=f'{meth}(numbers)', number=100,
                        setup=f'import random\nfrom __main__ import {meth}\nrandom.seed({trial})\nnumbers = {numbers}')/100
            ascending[meth] = timeit.timeit(stmt=f'{meth}(numbers)', number=100,
                        setup=f'import random\nfrom __main__ import {meth}\nrandom.seed({trial})\nnumbers = list(range({trial}))')/100

        results1 = '\t'.join(f'{counts[meth]:.3f}' for meth in methods)
        results2 = '\t'.join(f'{ascending[meth]:.3f}' for meth in methods)
                       
        print (f'{trial}\t{results1}\t{results2}')

if __name__ == '__main__':
    print ("Average Performance Times")
    outputPerformanceTiming()
    print ()
    print ("Construction Times")
    outputConstructionTiming()
    print ()
    print ("Stress Test Performance")
    stressTestTiming()
    
