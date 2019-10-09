"""
    Shows WordLadder implementation in Python, using Graph

    Which is faster? Try all possible four letter words, one at a time,
    or check all words in the graph? N=5875 four letter words

    Longest computed word ladder below:

    ['ABRI', 'ABSI', 'ASSI', 'ASSE', 'ARSE', 'ERSE', 'ELSE', 'ELLE',
     'ALLE', 'ALLS', 'ALPS', 'AMPS', 'IMPS', 'IMPY', 'IMMY', 'ISMY', 'ISMS']
    
    Author: George Heineman
"""
import networkx as nx
import unittest
import sys
import timeit

from datetime import datetime

from collections import deque

# Contains words, all in lower case.
wordFile = "words.english.txt"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"


class DepthFirstSearch:
    """
    Maintain DepthFirstSearch state using Stack.
    """
    def __init__(self, G):
        self.G = G

    def trail(self, pred, end):
        """Return list of words from source to end"""
        trail = []
        node = end
        while node:
            trail.insert(0, node)
            node = pred[node]
        return trail

    def wordLadder(self, start, end):
        """
        Identify word ladder using DepthFirstSearch, should it exist.
        """
        if start == end:
            return [start]
        
        active = deque()
        visited = {}
        pred = {}
        
        active.append(start)
        visited[start] = True
        pred[start] = None
        while active:
            u = active.pop()    # Treat like a stack
            
            for n in self.G.neighbors(u):
                if not n in visited:
                    visited[n] = True
                    pred[n] = u
                    if n == end:
                        return self.trail(pred, end)
            
                    active.append(n)
        return None


class BreadthFirstSearch:
    """
    Maintain BreadthFirstSearch state using Queue.
    """
    def __init__(self, G):
        self.G = G

    def trail(self, pred, end):
        """Return list of words from source to end"""
        trail = []
        node = end
        while node:
            trail.insert(0, node)
            node = pred[node]
        return trail

    def wordLadder(self, start, end):
        """
        Identify word ladder using BreadthFirstSearch, should it exist.
        """
        if start == end:
            return [start]
        
        active = deque()
        visited = {}
        pred = {}
        
        active.append(start)
        visited[start] = True
        pred[start] = None
        while active:
            u = active.popleft()
            if u == end:
                return self.trail(pred, end)
            
            for n in self.G.neighbors(u):
                if not n in visited:
                    visited[n] = True
                    pred[n] = u
                    active.append(n)
        return None

class Explore:
    """
    Explore Graph to find Word Ladder connected subsets that are disjoint,
    such that it is impossible to form a word ladder from A to B, but you
    can form a word ladder from C to D and these are all four letter words.

    Note words (such as ADZE) which belong to no word ladder are not counted.
    """
    def __init__(self, G):
        self.G = G
        self.sets = {}
        self.visited = {}
        self.samples = {}
        self.explore()

    def report(self):
        """Report the results of the exploration."""
        print ("Disjoint subsets of Word Ladders")
        for key in self.sets:
            print (str(key) + " -> " + str(self.sets[key]) + " with sample of " + str(self.samples[key]))
        
    def explore(self):
        """
        Count number of unique disjoint subsets of nodes
        """
        index = 0
        for n in self.G.nodes:
            if not n in self.visited and self.G.degree(n) > 0:
                index += 1
                active = deque()
                numFound = 0
                sample = []
                active.append(n)
                
                self.visited[n] = index
                while active:
                    u = active.pop()   
                    numFound += 1
                    if numFound < 5:
                        sample.append(u)
                    for w in self.G.neighbors(u):
                        if not w in self.visited:
                            self.visited[w] = index
                            active.append(w)
                self.sets[n] = numFound
                self.samples[n] = sample
             

def loadGraph(wordList):
    """
    Return the Graph representing all four letter words.
    """
    G = nx.Graph()
    with open(wordList) as fp:
       line = fp.readline()
       while line:
           word = line[:-1].upper()
           if len(word) == 4:
               G.add_node(word)
           line = fp.readline()


    # Now create edges. For each word, see if there is a corresponding
    # word by altering each position
    for node in list(G.nodes):
        for pos in range(4):
            actual = node[pos]
            for letter in alphabet:
                if actual != letter:
                    newWord = node[0:pos] + letter + node[pos+1:]
                    if node > newWord and newWord in G.nodes:
                        G.add_edge(node, newWord)

    return G

def longestWordLadderCheckAPSP(G):
    """
    Use Dijkstra's shortest_path to find the longestPath that exists
    within the Graph.
    """
    results = dict(nx.all_pairs_shortest_path(G))
    longest = 0
    longestPath = []
    allNodes = list(G.nodes)
    for src in range(0, len(allNodes)-1):
        srcNode = allNodes[src]
        for target in range(src+1, len(allNodes)):
            tgtNode = allNodes[target]
            if srcNode in results and tgtNode in results[srcNode]:
                path = results[srcNode][tgtNode]
                if len(path) > longest:
                    longest = len(path)
                    longestPath = path
    
    return longestPath

def computedLadder(edgeTo, start, end):
    """
    Starting at 'end' work backwards to 'start' using edgeTo links,
    and prepend so in order when done
    """
    node = end
    ladder = []
    while node != start:
        ladder.insert(0, node)
        node = edgeTo[node]

    ladder.insert(0, start)
    return (ladder)

def wordLadderBFS_deque(G, start, end):
    """
    Identify word ladder using Breadth first search, should it exist.
    https://docs.python.org/2/library/collections.html
    """
    marked = {}
    edgeTo = {}

    from collections import deque
    Q = deque([start])
    while Q:
        v = Q.popleft()

        if v == end:
            return computedLadder(edgeTo, start, end)
        
        for w in G.adj[v]:
            if not w in marked:
                edgeTo[w] = v
                marked[w] = True
                Q.append(w)
    return []

def noWordLadders(G):
    """Identify those nodes that do not participate in any word ladder."""
    for n in G.nodes:
        if G.degree(n) == 0:
            yield n

def floydWarshall(G):
    """
    Use Floyd-Warshall algorithm to compute dist[u][v] and return dist[]
    """
    n = G.number_of_nodes()
    pred = [[0] * n for i in range(n)]
    dist = [[0] * n for i in range(n)]
    
    # map each node to an integer 0 .. n-1
    count = 0
    index = {}
    allNodes = list(G.nodes)
    for node in allNodes:
        index[node] = count
        count += 1
  
    # initialize
    for ui in range(n):
        for vi in range(n):
            dist[ui][vi] = sys.maxsize
            pred[ui][vi] = None

        dist[ui][ui] = 0
        u = allNodes[ui]
        for v in G.adj[u]:
            vi = index[v]
            dist[ui][vi] = 1    # an edge exists
            pred[ui][vi] = ui

    # process by sweeping through
    print (str(datetime.now()))
    for ki in range(n):
        for ui in range(n):
            for vi in range(n):
                newLen = dist[ui][ki] + dist[ki][vi]
                if newLen < dist[ui][vi]:
                    dist[ui][vi] = newLen
                    pred[ui][vi] = pred[ki][vi]
                    
    print (str(datetime.now()))

    # Find longest value in dist[]
    maxFound = 0
    maxi = maxj = -1
    for i in range(n):
        for j in range(n5):
            if dist[i][j] > maxFound:
                maxFound = dist[i][j]
                maxi = i
                maxj = j
    
    return wordLadderBFS_deque(G, allNodes[maxi], allNodes[maxj])


def loadDefaultGraph():
    return loadGraph(wordFile)

if __name__ == '__main__':
    print (str(datetime.now()))
    G = loadGraph(wordFile)

    nowl = list(noWordLadders(G))
    print ("Following " + str(len(nowl)) + " words belong to no word ladder.")
    print (nowl)

    e = Explore(G)
    e.report()
    
    BFS = BreadthFirstSearch(G)
    wl = BFS.wordLadder('COLD', 'WARM')
    print (wl)
    print (len(wl))
    
    DFS = DepthFirstSearch(G)
    wl = DFS.wordLadder('COLD', 'WARM')   
    print (wl)
    print (len(wl))
    
    print (" All Pairs Shortest Path\n" + str(datetime.now()))
    longest = longestWordLadderCheckAPSP(G)
    for w in longest:
        print (w + "\tDegree=" + str(G.degree(w)))

    print (" Floyd Warshall Done\n" + str(datetime.now()))
    print (floydWarshall(G))
    print ("\n" + str(datetime.now()))
    


