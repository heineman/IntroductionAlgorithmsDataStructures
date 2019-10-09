"""
    Start with four-letter word; goal is to reach another four letter
    word by changing one letter at a time (while forming only real words)
    until the goal is reached.

    Use queue for storage with three different implementations.

    Timing code passes in function to use for checking whether a word exists.
    This code is used to experiment with variety of options and shows
    the time results.
    
    Author: George Heineman
"""
import unittest
import sys
import timeit

from datetime import datetime

# Contains words, all in lower case.
wordFile = "words.english.txt"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"

class Stage:
    """A Stage in the word ladder, recording prior word (which defaults to None)."""
    def __init__(self, word, prior = None):
        self.word = word
        self.prior = prior

    def collectTrail(self):
        """Return list of words from source to end"""
        trail = []
        node = self
        while node:
            trail.insert(0, node.word)
            node = node.prior
        return trail

def isWordInDictionary(d, word):
    """Determine if word is valid based on dictionary."""
    return word in d

def isWordInList(aList, word):
    """Determine if word is valid based on a list."""
    return word in aList

def isWordInSortedList(aList, tgt):
    """Determine if word is valid using BinaryArraySearch on sorted list."""
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

def loadWordsAsDictionary(wordList):
    """
    Return Dictionary of four-letter words to explore, each with
    a count of zero.
    """
    words = {}
    with open(wordList) as fp:
       line = fp.readline()
       
       while line:
           word = line[:-1].upper()
           if len(word) == 4:
               words[word] = 0
               
           line = fp.readline()
    return words

def loadWordsAsList(wordList):
    """
    Return list of four-letter words to explore.
    """
    words = []
    with open(wordList) as fp:
       line = fp.readline()
       
       while line:
           word = line[:-1].upper()
           if len(word) == 4:
               words.append(word)
               
           line = fp.readline()
    return words

def neighbors(word, words, isWord):
    """Return valid neighboring 4-letter words of given word."""
    neighbors = []
    for let in alphabet:
        for pos in range(0,4):
            newWord = word[0:pos] + let + word[pos+1:]
            if isWord(words, newWord) and newWord != word:
                neighbors.append(newWord)
                
    return neighbors

def exploreQueueList(words, start, end, isWord):
    """Using existing collection of words, find ladder from start to end"""
    if not start in words:
        raise Exception (start + " is not a valid four-letter word.")
    if not end in words:
        raise Exception (end + " is not a valid four-letter word.")

    active = []
    active.append(Stage(start))
    
    while active:
        st = active.pop(0)
            
        for nxt in neighbors(st.word, words, isWord):
            link = Stage(nxt, st)
            if nxt == end:
                return link
            active.append(link)

    # No chain
    return []


def exploreQueueQueue(words, start, end, isWord):
    """Using existing collection of words, find ladder from start to end."""
    if not start in words:
        raise Exception (start + " is not a valid four-letter word.")
    if not end in words:
        raise Exception (end + " is not a valid four-letter word.")

    from queue import Queue
    active = Queue()
    active.put(Stage(start))
    
    while active:
        st = active.get()
            
        for nxt in neighbors(st.word, words, isWord):
            link = Stage(nxt, st)
            if nxt == end:
                return link
            active.put(link)

    # No chain
    return []

def exploreQueueDQ(words, start, end, isWord):
    """Using existing collection of words, find ladder from start to end."""
    if not start in words:
        raise Exception (start + " is not a valid four-letter word.")
    if not end in words:
        raise Exception (end + " is not a valid four-letter word.")

    from collections import deque
    active = deque()
    active.append(Stage(start))
    
    while active:
        st = active.popleft()
            
        for nxt in neighbors(st.word, words, isWord):
            link = Stage(nxt, st)
            if nxt == end:
                return link
            active.append(link)

    # No chain
    return []

def outputTiming(start, end):
    """
    Generate timing report for the three different approaches.
    """
    print ('Queue\tList\tBASearch\tDictionary')

    trials = ['L', 'SL', 'D']
    loadMethods = ['loadWordsAsList', 'loadWordsAsList', 'loadWordsAsDictionary']
    valids = ['isWordInList', 'isWordInSortedList', 'isWordInDictionary' ]
    countsDQ = {}
    countsList = {}
    countsQueue = {}
    for trial,load,valid in zip(trials,loadMethods,valids):
        countsDQ[trial] = timeit.timeit(stmt=f'exploreQueueDQ(words,"{start}","{end}",{valid})', number=5,
                setup=f'from __main__ import {valid},{load},exploreQueueDQ,wordFile\nwords={load}(wordFile)')
        countsList[trial] = timeit.timeit(stmt=f'exploreQueueList(words,"{start}","{end}",{valid})', number=5,
                setup=f'from __main__ import {valid},{load},exploreQueueList,wordFile\nwords={load}(wordFile)')
        countsQueue[trial] = timeit.timeit(stmt=f'exploreQueueQueue(words,"{start}","{end}",{valid})', number=5,
                setup=f'from __main__ import {valid},{load},exploreQueueQueue,wordFile\nwords={load}(wordFile)')

    print ("DQ\t" + '\t'.join(f'{countsDQ[trial]:f}' for trial in trials))
    print ("List\t" + '\t'.join(f'{countsList[trial]:f}' for trial in trials))
    print ("Q\t" + '\t'.join(f'{countsQueue[trial]:f}' for trial in trials))

if __name__ == '__main__':
    outputTiming('COLD', 'WARM')


