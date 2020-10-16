import networkx as nx
import graph6
import graph7
import graph8
import graph9
import graph10


def bfs(G,a,b):
    G.add_nodes_from(G.nodes(), label = -1) # initialization of all labels
    G.nodes[a]['label'] = 0

    nodeLayer = 0
    while G.nodes[b]["label"] == -1:
        # Find all the nodes in the current layer
        layerNodes = (
            node
            for node in G
            if G.nodes[node]["label"] == nodeLayer
        )

        # Find all the unvisited neighbours of the nodes in this layer.
        # I use set() to remove repeated neighbours
        unlabelledNeighbours = set(
            neighbour
            for node in layerNodes
            for neighbour in G[node]
            if G.nodes[neighbour]["label"] == -1
        )

        nodeLayer += 1

        # Set the node layer for each of the unlabelled neighbours
        for neighbour in unlabelledNeighbours:
            G.nodes[neighbour]["label"] = nodeLayer

    return G.nodes[b]["label"]


# region Lecturer's Code
G6=graph6.Graph()
a=12
b=40
print('Graph G6:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G6,a,b))
print()

G7=graph7.Graph()
a=5
b=36
print('Graph G7:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G7,a,b))
print()

G8=graph8.Graph()
a=15
b=35
print('Graph G8:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G8,a,b))
print()

G9=graph9.Graph()
a=1
b=19
print('Graph G9:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G9,a,b))
print()

G10=graph10.Graph()
a=6
b=30
print('Graph G10:')
print('The distance between vertices', a, 'and', b, 'is:', bfs(G10,a,b))
print()

# endregion Lecturer's Code

