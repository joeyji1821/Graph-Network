import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

tuple1 = (1, 2, 3)
tuple2 = (2, 2, 3)

a = np.array(((3, 2, 3), (4, 2, 3), (5, 2, 3)))
list_of_tuples = list(map(tuple, a))

G = nx.DiGraph()
G.add_node(tuple1) # any hashable can be a node
G.add_node(tuple2)
G.add_edge(tuple1, tuple2) # default edge data=1
G.add_nodes_from(list_of_tuples)
G.add_edge(tuple1, (3, 2, 3))
G.add_edge(tuple2, (4, 2, 3))
G.add_edge((4, 2, 3), (5, 2, 3))

print(nx.dijkstra_path(G, tuple1, (5, 2, 3)))


nx.draw_planar(G, with_labels = True) # default spring_layout
plt.show()