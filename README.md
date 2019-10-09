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

## Comparison to Sorting Methods

```
cd "3. Sorting Algorithms"
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
N       Insert  Merge   Tim
16      0.0020  0.0068  0.0001
32      0.0070  0.0152  0.0003
64      0.0302  0.0333  0.0006
128     0.0943  0.0729  0.0011
256     0.3889  0.1614  0.0022
512     1.7536  0.3729  0.0048
1024    7.3282  0.8242  0.0106
2048    28.7848 1.7879  0.0237
4096    0.0000  3.8638  0.0508
8192    0.0000  8.1089  0.1141
16384   0.0000  17.0846 0.2484
32768   0.0000  35.9748 0.5271
```

The first two lines of output briefly confirm InsertionSort and MergeSort
are working. The table compares the performance of the three sorting
algorithms when sorting a list formed by concatenating (1) N sorted integers
from 0 to N-1; with (2) N/4 sorted integers randomly samples from the range
(0, N/4).

TimSort is almost two orders of magnitude faster.

## Tasks to Solve 1, 2,3

This code takes the longest to run. 

First it solves Task #2, finding 60 words that belong to no word ladder.

I'm glad to see that it is impossible to form a word ladder from 'GOOD' to
'EVIL'.

Second, it solves Task #4, finding disjoint subsets of non-connectable
words. Of the 5,875 four-letter words, it is possible to form a word ladder
between any two of 5,807 words. There are three smaller "islands" that are
formed by smaller subsets, as you can see.

It then solves the 'COLD' -> 'WARM' Word Ladder using a BreadthFirstSearch,
which results in a Word Ladder of 5 words. Using DepthFirstSearch, the
resulting word ladder has 392 words.


```
Following 60 words belong to no word ladder.
['ADZE', 'AKOV', 'ANKH', 'AWFU', 'AWOL', 'CEYX', 'DEGU', 'EBBS', 'ECRU',
'EFIK', 'EJOO', 'EKOI', 'ELHI', 'ENIF', 'ENKI', 'ENVY', 'EPEE', 'EPHA',
'ERUC', 'ESOX', 'ETYM', 'EVIL', 'EXPO', 'HEXA', 'HOJU', 'HYMN', 'IGLU',
'IJMA', 'IMAM', 'ISBA', 'ITYS', 'IVIN', 'JEUX', 'JISM', 'JUJU', 'LLYN',
'LWEI', 'NGAI', 'NIOG', 'OCHT', 'ODSO', 'OGPU', 'OHMS', 'OLPE', 'OMAO',
'OPSY', 'PFFT', 'PFUI', 'SYBO', 'TSIA', 'UBII', 'UGHS', 'ULMO', 'UPBY',
'UPON', 'VLEI', 'VULN', 'WROX', 'YCIE', 'ZYGA']
Disjoint subsets of Word Ladders
AAHS -> 5807 with sample of ['AAHS', 'HAHS', 'HEHS', 'PEHS']
EPPY -> 2 with sample of ['EPPY', 'ESPY']
ERYX -> 4 with sample of ['ERYX', 'ORYX', 'ONYX', 'ONYM']
GEGG -> 2 with sample of ['GEGG', 'YEGG']
['COLD', 'CORD', 'CARD', 'WARD', 'WARM']
5
['COLD', 'WOLD', 'WORD', 'WORT', 'WOWT', 'YOWT', 'YOWS', 'YOKS', 'YUKS',
'YUPS', 'YIPS', 'ZIPS', 'ZITS', 'ZITI', 'ZATI', 'YATI', 'YETI', 'YETT',
'YEST', 'YESO', 'PESO', 'PISO', 'PIST', 'WIST', 'WUST', 'WUSS', 'WYSS',
'WYNS', 'WYNE', 'WYVE', 'WOVE', 'WOTE', 'YOTE', 'YORE', 'YERE', 'YERN',
'YIRN', 'YIRR', 'YARR', 'YARU', 'YABU', 'YABA', 'YAYA', 'YAYS', 'YAMS',
'YAMP', 'YAWP', 'YAWY', 'JAWY', 'JEWY', 'PEWY', 'PEWS', 'TEWS', 'TEWA',
'TERA', 'VERA', 'VIRA', 'VIVA', 'VIVE', 'VISE', 'VASE', 'WASE', 'WESE',
'WEDE', 'WIDE', 'WIRE', 'WIRY', 'WINY', 'WINO', 'VINO', 'VINT', 'VENT',
'WENT', 'WEPT', 'SEPT', 'SEXT', 'TEXT', 'TELT', 'TOLT', 'VOLT', 'VOLE',
'SOLE', 'SOPE', 'TOPE', 'TYPE', 'TYRE', 'TYRR', 'TYER', 'TYES', 'TOES',
'WOES', 'WOPS', 'WAPS', 'WAWS', 'WAWL', 'WAUL', 'WAUR', 'WAIR', 'WHIR',
'WHIZ', 'WHUZ', 'WHUN', 'WHEN', 'WREN', 'WRAN', 'WRAW', 'DRAW', 'DROW',
'TROW', 'TROY', 'TREY', 'TRET', 'TRYT', 'TRYP', 'TRIP', 'TRIO', 'THIO',
'THRO', 'TORO', 'TOYO', 'MOYO', 'MOZO', 'KOZO', 'KOTO', 'ROTO', 'ROTS',
'SOTS', 'SOYS', 'SOYA', 'SORA', 'SURA', 'SURF', 'TURF', 'TURP', 'TUMP',
'TUME', 'TUTE', 'TUTU', 'TUNU', 'TUNY', 'TONY', 'TOWY', 'TOWN', 'TOON',
'ZOON', 'ZOOS', 'MOOS', 'MOSS', 'POSS', 'POSY', 'ROSY', 'ROXY', 'RIXY',
'RIMY', 'RIMU', 'LIMU', 'LITU', 'MITU', 'MITY', 'PITY', 'PITH', 'WITH',
'WICH', 'WICK', 'WILK', 'WULK', 'WULL', 'WELL', 'YELL', 'YILL', 'ZILL',
'ZOLL', 'ROLL', 'ROOL', 'WOOL', 'WOOM', 'WHOM', 'WHOP', 'WHAP', 'WHAT',
'THAT', 'TWAT', 'TWIT', 'TWIN', 'TAIN', 'ZAIN', 'ZEIN', 'VEIN', 'VEIL',
'VEAL', 'VIAL', 'VIOL', 'SIOL', 'SION', 'SLON', 'SLOW', 'SWOW', 'SWOT',
'STOT', 'STUT', 'STUN', 'STEN', 'STEY', 'STAY', 'SWAY', 'SWAP', 'SWEP',
'SKEP', 'SKIP', 'SNIP', 'SNUP', 'SOUP', 'YOUP', 'YOUR', 'TOUR', 'TOUG',
'TRUG', 'TRUN', 'GRUN', 'GRUS', 'URUS', 'URNS', 'URNA', 'URVA', 'ULVA',
'ULLA', 'OLLA', 'OLEA', 'PLEA', 'PLEX', 'PREX', 'PREP', 'PROP', 'PROS',
'PHOS', 'THOS', 'THUS', 'THUD', 'CHUD', 'CRUD', 'CRUX', 'CRAX', 'CRAP',
'FRAP', 'FRAY', 'PRAY', 'PRAT', 'PRUT', 'POUT', 'ROUT', 'ROUX', 'DOUX',
'DOUM', 'DRUM', 'DRUB', 'DRIB', 'FRIB', 'FRIT', 'WRIT', 'WRIG', 'PRIG',
'PRIM', 'PLIM', 'SLIM', 'SWIM', 'SWUM', 'SCUM', 'SCUR', 'SPUR', 'SPUG',
'SPIG', 'SPIV', 'SHIV', 'SHIT', 'SUIT', 'YUIT', 'YURT', 'HURT', 'HURR',
'PURR', 'PURU', 'PULU', 'SULU', 'SUSU', 'SUSI', 'SUJI', 'FUJI', 'FUCI',
'FUCK', 'YUCK', 'YUCH', 'YECH', 'YEAH', 'YEAS', 'YENS', 'LENS', 'LINS',
'TINS', 'TINK', 'ZINK', 'ZONK', 'ZONE', 'RONE', 'RUNE', 'SUNE', 'SUNS',
'SUMS', 'SUMO', 'SUTO', 'AUTO', 'ALTO', 'ALTS', 'ARTS', 'ORTS', 'OUTS',
'PUTS', 'PUTZ', 'FUTZ', 'FUZZ', 'HUZZ', 'HIZZ', 'SIZZ', 'SIZY', 'SIDY',
'TIDY', 'TIVY', 'TAVY', 'WAVY', 'WALY', 'WALI', 'WADI', 'SADI', 'SARI',
'VARI', 'VARY', 'VADY', 'LADY', 'LAZY', 'MAZY', 'MAZE', 'RAZE', 'RAVE',
'SAVE', 'SATE', 'SITE', 'SITA', 'SINA', 'SINH', 'SISH', 'SOSH', 'TOSH',
'TUSH', 'TUSK', 'TUIK', 'TUIS', 'TUGS', 'VUGS', 'VUGH', 'AUGH', 'AUGE',
'LUGE', 'LURE', 'MURE', 'MUSE', 'MUSA', 'RUSA', 'RUTA', 'RUTH', 'RUKH',
'RAKH', 'RASH', 'RESH', 'RESP', 'RISP', 'RISS', 'RIGS', 'REGS', 'SEGS',
'SESS', 'SASS', 'TASS', 'TATS', 'VATS', 'VETS', 'WETS', 'WETA', 'WEKA',
'WEKI', 'WERI', 'WERF', 'WARF', 'WARM']
392
 All Pairs Shortest Path
ABRI	   Degree=1
ABSI	   Degree=2
ASSI	   Degree=3
ASSE	   Degree=4
ARSE	   Degree=3
ERSE	   Degree=6
ELSE	   Degree=5
ELLE	   Degree=3
ALLE	   Degree=12
ALLS	   Degree=13
ALPS	   Degree=8
AMPS	   Degree=7
IMPS	   Degree=4
IMPY	   Degree=3
IMMY	   Degree=3
ISMY	   Degree=2
ISMS	   Degree=1
 Floyd Warshall Done
```

Using the NetworkX built-in support for Dijkstra's All Pairs Shortest Path
algorithm, we can discover the longest Word Ladder in this dictionary
contains 17 words.
