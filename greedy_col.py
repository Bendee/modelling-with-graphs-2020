import networkx as nx
import graph1
import graph2
import graph3
import graph4
import graph5


def find_smallest_colour(G, i):
    # Finds the set of colours currently used by the nodes neighbours
    # I use set() as it removes repeated colours
    neighbourColours = sorted(set(
        G.nodes[neighbour]["colour"]
        for neighbour in G[i]
        if G.nodes[neighbour]["colour"] != "never coloured"
    ))

    # Chooses the lowest possible value as the colour to use
    colour = next(
        index
        # The [None] is in the case that the list of neigbour colours is empty.
        for index, value in enumerate(neighbourColours + [None], 1)
        if index != value
    )

    return colour


def greedy(G):
    kmax = 0

    for node in G:
        colour = find_smallest_colour(G, node)
        # If the maximum colour has to be increased, increase it
        if colour > kmax:
            kmax = colour

        G.nodes[node]["colour"] = colour

# region Lecturer's Code
    print()
    for i in G.nodes():
        print('vertex', i, ': colour', G.nodes[i]['colour'])
    print()
    print('The number of colors that Greedy computed is:', kmax)


print('Graph G1:')
G=graph1.Graph()
greedy(G)

print('Graph G2:')
G=graph2.Graph()
greedy(G)

print('Graph G3:')
G=graph3.Graph()
greedy(G)

print('Graph G4:')
G=graph4.Graph()
greedy(G)

print('Graph G5:')
G=graph5.Graph()
greedy(G)

# endregion Lecturer's Code

