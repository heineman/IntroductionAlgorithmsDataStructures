# IntroductionAlgorithmsDataStructures
This repository contains the code associated with the "Introduction to Algorithms and Data Structures" Safari Video. https://www.oreilly.com/live-training/courses/introduction-to-algorithms-and-data-structures/0636920306535/

## Code Examples

The code examples are referred to in the slides.  Here are sample
executions. All examples are derived by running Python 3.6 on Linux.
Start in the current directory and change directory (cd) into the different
subdirectories to execute the code as you see below.

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

