import networkx as nx
import matplotlib.pyplot as plt

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWYXZ"
inFile = open("words.english.txt", "r")
wordList = inFile.read().splitlines()

words = {}
for word in wordList:
    words[word] = 0

def neighbors(word):
    """Return valid neighboring 4-letter words of given word."""
    found = []
    for let in alphabet:
        for pos in range(0,4):
            newWord = word[0:pos] + let + word[pos+1:]
            if newWord in words and newWord != word:
                found.append(newWord)
                
    return found

def createGraph(allWords):
    """Pass in a list of four-letter words."""
    G = nx.Graph()
    for w in allWords:
        G.add_node(w)

    # Now create edges by considering neighbors of each word. Use fast neighbors implementation!
    for node in list(G.nodes()):
        for n in neighbors(node):
            if n > node:
                G.add_edge(n, node)

    return G

wordGraph = createGraph(wordList)

nx.draw(wordGraph, with_labels=True)
plt.show()

