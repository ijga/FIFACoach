from graph import Graph
import networkx as nx
import matplotlib.pyplot as plt
import pickle

GAME = 1

def visualize_graph(graph: Graph):
    G = nx.Graph()

    for game_object in graph.get_all_graph_objects():
        G.add_node(game_object.id, pos=(game_object.x, game_object.y))

    for edge in graph.get_all_edges():
        G.add_edge(edge.player.id, edge.target.id)

    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=12)
    plt.show()


with open(f"unlabeled_graphs/game{GAME}.pickle", "rb") as unlabeled:
    for idx in range(10000):          
        graph: Graph = pickle.load(unlabeled)
        visualize_graph(graph)