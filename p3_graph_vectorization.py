import pickle
from graph import Graph
import torch
from torch_geometric.data import InMemoryDataset, download_url

GAME = "1"
ITER = "1"
FRAMES = 54120
VID_STRIDE=90
PICKLE_LENGTH = FRAMES//VID_STRIDE

# open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_graph_indicator.txt", "w")
# open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_node_attributes.txt", "w")
# open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_edges.txt", "w")
# open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_edge_attributes.txt", "w")
# open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_graoh_labels.txt", "w")

with open(f"labeled_graphs/game{GAME}_{ITER}.pickle", "rb") as labeled:
    nodes_from_prev_graphs = 0
    edges_from_prev_graphs = 0
    
    for i in range(PICKLE_LENGTH):
                
        graph: Graph = pickle.load(labeled)

        # n = total number of nodes
        # m = total number of edges
        # N = number of graphs

        nodes_in_current_graph = 0

        with open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_graph_indicator.txt", "a") as graph_indicator:  # n
            with open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_node_attributes.txt", "a") as node_attributes:  # n
                for graph_object in graph.get_all_graph_objects():  # go through all nodes
                    node_attributes.write(graph_object.create_feature_vector(nodes_from_prev_graphs)+"\n")
                    graph_indicator.write(str(i)+"\n")
                    nodes_in_current_graph += 1

        edges_in_current_graph = 0

        with open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_edges.txt", "a") as edges:  # m
            with open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_edge_attributes.txt", "a") as edge_attributes:  # m
                for edge in graph.get_all_edges():  # go through all edges
                    edges.write(edge.create_sparse_adj_matrix_pair(nodes_from_prev_graphs)+"\n")
                    edge_attributes.write(edge.create_feature_vector()+"\n")
                    edges_in_current_graph += 1
        
        nodes_from_prev_graphs += nodes_in_current_graph
        edges_from_prev_graphs += edges_from_prev_graphs

        with open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_graph_labels.txt", "a") as graph_labels:  # N
            graph_labels.write(graph.get_classification()+"\n")
