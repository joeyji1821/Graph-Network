import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import csv


def TowersOfHanoi(layers):
    # creating the graph and the start and end point based on the number of layers
    # node convention: number of layers determines the dimension of each tuple,
    #  each index represent the tower the specific layer is on, i.e. (1, 1, 1):
    #   |      |     |
    #   -      |     |
    #  ---     |     |
    # -----    |     |
    G = nx.Graph()
    start = tuple([1] * layers)
    end = tuple([3] * layers)
    G.add_nodes_from(list(map(tuple, (start, end))))

    # mapping all possible node and path
    completedNetwork = makeAMove(start, end, G)

    plt.figure(figsize=(10, 10))
    # plt.figure(figsize = (50, 50))
    # plot out the network
    nx.draw_kamada_kawai(G, with_labels=True)  # default spring_layout
    print(nx.dijkstra_path(G, start, end))
    path1 = nx.shortest_path(G, source=start, target=end)
    path_edges1 = list(zip(path1, path1[1:]))
    pos = nx.kamada_kawai_layout(G)
    nx.draw_networkx_nodes(G, pos, nodelist=path1, node_color='r')
    nx.draw_networkx_edges(G, pos, edgelist=path_edges1, edge_color='r', width=10)
    plt.savefig("output_6_nodes.png")
    plt.show()

    # saves Adjacency Matrix, Incidence Matrix, and Eigenvector Centrality into an excel sheet
    centrality = nx.eigenvector_centrality(G)
    sorted_centrality = dict(sorted(centrality.items(), key=lambda item: item[1], reverse=True))
    header = 'node', 'eigenvector_centrality'
    with open('descending_order_eigenvector_centrality.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()
        for a, b in sorted_centrality.items():
            writer.writerow(dict(zip(header, (''.join(str(e) for e in list(a)), b))))

    print(G.nodes())
    print(G.edges())
    # print(",".join(str('<->'.join(str(''.join(str(a) for a in list(e)))) for e in G.nodes()      )))
    np.savetxt('adjacency_matrix.csv', nx.adjacency_matrix(G).todense(), delimiter=',', header=",".join(str(''.join(str(a) for a in list(e))) for e in G.nodes()), fmt='%s')
    np.savetxt('incidence_matrix.csv', nx.incidence_matrix(G).todense(), delimiter=',', header=",".join(str('<->'.join(str(''.join(str(b) for b in list(a))) for a in list(e))) for e in G.edges()), fmt='%s')
    # print(nx.adjacency_matrix(G))
    # print(nx.incidence_matrix(G))
    # print(nx.is_eulerian(G))


def makeAMove(node, end, G):
    # terminating condition
    if node == end:
        return G
    else:
        # going through layer by layer
        for x in range(0, len(node)):
            # make sure no smaller layer is on top of the layer we are trying to move
            if not node[0:x] or not any(i == node[x] for i in node[0:x]):
                # the layer is movable
                for y in range(1, 4):
                    # make sure layer is not trying to stay in the same pole
                    if node[x] != y:
                        # make sure no smaller layer is at the next possible destination
                        if not node[0:x] or not any(i == y for i in node[0:x]):
                            # make a new tuple after making the move to the new pole
                            tempList = list(node)
                            tempList[x] = y
                            tempTuple = tuple(tempList)
                            if not G.has_edge(node, tempTuple):
                                G.add_edge(node, tempTuple)
                                makeAMove(tempTuple, end, G)

TowersOfHanoi(3)


'''
modified = tuple([2, 2, 1, 3, 3, 1])
path2 = nx.shortest_path(G, source=modified, target=end)
path_edges2 = list(zip(path2, path2[1:]))
nx.draw_networkx_nodes(G, pos, nodelist=path2, node_color='g')
nx.draw_networkx_edges(G, pos, edgelist=path_edges2, edge_color='g', width=5)

print('Dictionary in ascending order by value : ', sorted_centrality)
print('Dictionary in original order by value : ', centrality)
print(list(sorted_centrality.values()))
'''
