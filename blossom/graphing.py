import networkx as nx
import matplotlib.pyplot as plt
from structures import Edge, Tree, Matching
from max_matching import max_matching

def create_graph_with_matching(n, nodes, edges, M):
    G = nx.Graph()
    G.add_nodes_from(nodes)

    for edge in edges:
        edge_color = 'b' if edge not in M.edges else 'r'
        G.add_edge(edge.start, edge.end, color=edge_color)

    return G.to_directed()

def create_graph(n, nodes, edges):
    return create_graph_with_matching(n, nodes, edges, Matching(n))

def show_graph(n, nodes, edges):
    G = create_graph(n, nodes, edges)
    nx.draw(G, with_labels=True)
    plt.show()

def find_and_show_max_matching(n, nodes, edges):
    matching = max_matching(nodes, edges)
    G = create_graph_with_matching(n, nodes, edges, matching)
    colors = nx.get_edge_attributes(G,'color').values()
    nx.draw(G, with_labels=True, edge_color=colors)
    plt.show()