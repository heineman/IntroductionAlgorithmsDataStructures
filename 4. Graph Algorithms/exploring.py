# Explore graphs

import networkx as nx

G = nx.Graph()

G.add_edge(0, 1)
G.add_edge(0, 2)
G.add_edge(1, 3)
G.add_edge(1, 4)
G.add_edge(2, 5)
G.add_edge(3, 4)
G.add_edge(3, 5)
G.add_edge(4, 7)
G.add_edge(5, 6)
G.add_edge(6, 7)

# Compute shortest paths
results = dict(nx.all_pairs_shortest_path(G))
print ('    s 1 2 3 4 5 6 t')
print ('    - - - - - - - -')   
for u in range(8):
    print(str(['s', 1, 2, 3, 4, 5, 6, '7'][u]) + ": ", end=' ')
    for v in range(8):
        print(len(results[u][v])-1, end=' ')
    print()
    
    




