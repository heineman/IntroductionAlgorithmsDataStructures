# IntroductionAlgorithmsDataStructures
This repository contains the code associated with the "Introduction to Algorithms and Data Structures" Safari Video. https://www.oreilly.com/live-training/courses/introduction-to-algorithms-and-data-structures/0636920306535/

## Code Examples

The code examples are referred to in the slides.  Here are sample
executions. All examples are derived by running Python 3.6 on Linux.
Start in the current directory and change directory (cd) into the different
subdirectories to execute the code as you see below. Note that the 
run-time and performance numbers in this README file will not exactly 
match the empirical numbers in the slides because, as you should know,
your mileage may vary when running this code on different operating
systems and machines.

## Algorithm Formalities

The first section covers at a high level the mathematical formalisms used
to measure the time complexity and space complexity of various
algorithms. This is a rather informal presentation of fundamental concepts
that have been extensively studied for decades. For the most part, the Big
O notation I present characterizes the performance or space expectations in
the worst case.

```
$ cd "1. log(n) behavior"
$ python3 timing.py
N       Sum             Set             String          Loop
2       0.000340        0.000719        0.001278        0.001356
4       0.000469        0.001087        0.002519        0.002853
8       0.000732        0.001887        0.004891        0.007287
16      0.001322        0.003326        0.011106        0.022486
32      0.002428        0.007014        0.024445        0.079047
64      0.004606        0.012505        0.062425        0.288615
128     0.009418        0.026903        0.173157        1.107360
256     0.018405        0.050565        0.552694        4.365471
512     0.036613        0.111584        1.869063        19.802331
1024    0.072648        0.205249        6.836513        81.542065
```

* Sum adds n numbers together
* Set uses a Python <tt>set</tt> to check if list contains duplicate
* String constructs a large string from list to see if it contains a
  duplicate value
* Loop uses a doubly-nested loop to check if list contains duplicate values.

This code example doesn't appear in the slides

```
$ cd "1. log(n) behavior"
$ python3 timingContains.py
N       Contains        SortContains    BinaryArraySearch
2       0.002215        0.004460        0.009865
4       0.002665        0.006678        0.012944
8       0.003542        0.010472        0.015342
16      0.005451        0.018023        0.017826
32      0.008994        0.033644        0.020851
64      0.016200        0.063886        0.023410
128     0.029997        0.126325        0.026265
256     0.059538        0.247645        0.030780
512     0.120109        0.499623        0.042858
1024    0.235471        1.022691        0.046437
2048    0.488453        2.021996        0.050133
4096    0.993467        4.089057        0.053896
8192    2.013314        8.130922        0.058048
16384   4.024054        16.326974       0.061534
32768   8.151769        33.002672       0.065873
```

This table empirically evaluates code to "Check if List Contains a Target
Integer."

* Contains use the python <b>in</b> operator
* SortContains uses a linear sort over a sorted list
* BinaryArraySearch over a sorted list

## Performance Comparison

```
cd "2. Basic Data Structures"
$ python3 queueWordLadder.py
['COLD', 'CORD', 'CARD', 'WARD', 'WARM']

List            BASearch        Dictionary
412.751261      14.179721       2.790587
```

This code uses a stand-along <b>queue</b> to compute a Word Ladder between
'COLD' and 'WARM'. When determining whether a four-letter word is a valid
English word, there are three possibile approaches:

* Use a Python list to store all words and check using <b>in</b>
* Use a Sorted List and use BinaryArraySearch
* Use a Python dictionary

## Word Ladder Summary

```
cd "2. Basic Data Structures"
$ python3 queueTimingThreeWordLadder.py
Queue   List            BASearch        Dictionary
DQ      405.722967      14.274099       2.756425
List    407.715855      14.827824       3.329750
Q       409.225666      17.220676       5.669427
```

This code choose three different data structures to store the queue. The
impact is marginal. When considering the fastest option for checking
whether a four-letter word is a valid English word (Dictionary) the three
different implementations show how the <b>deque</b> offers the best
implementation. The <b>list</b> implementation is next, and the
<b>queue</b> implementation a distant third, because of the overhead from
supporting thread-safe operations.

