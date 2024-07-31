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
    highest_id_in_last_graph = 0
    graph_num = 0
    
    for i in range(PICKLE_LENGTH):
                
        graph: Graph = pickle.load(labeled)

        # n = total number of nodes
        # m = total number of edges
        # N = number of graphs

        highest_id_in_graph = 0

        node_id_remapping = {}  # for every graph, make a map with old_id:new_id when writing nodes, 
                                # and then pass that into create_sparse_adj_matric_pair to make sure edges are updated
                                # need to be 0 based

        node_remapped_inc = 0

        with open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_graph_indicator.txt", "a") as graph_indicator:  # n
            with open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_node_attributes.txt", "a") as node_attributes:  # n
                # with open(f"vectorized_graphs/game{GAME}_{ITER}/check.txt", "a") as check:  # n
                for graph_object in graph.get_all_graph_objects():  # go through all nodes
                    node_attributes.write(graph_object.create_feature_vector()+"\n")
                    graph_indicator.write(str(graph_num)+"\n")
                    node_id_remapping[graph_object.id] = highest_id_in_last_graph + node_remapped_inc
                        # check.write(str(graph_object.id) + " " + str(highest_id_in_last_graph + node_remapped_inc) + "\n")
                    node_remapped_inc += 1
                if graph.is_not_empty():
                    graph_num += 1

        with open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_edges.txt", "a") as edges:  # m
            with open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_edge_attributes.txt", "a") as edge_attributes:  # m
                for edge in graph.get_all_edges():  # go through all edges. There cannot be edges without nodes
                    edges.write(edge.create_sparse_adj_matrix_pair_remap(node_id_remapping)+"\n")
                    edge_attributes.write(edge.create_feature_vector()+"\n")
        
        highest_id_in_last_graph += node_remapped_inc

        with open(f"vectorized_graphs/game{GAME}_{ITER}/FIFAGS_graph_labels.txt", "a") as graph_labels:  # N
            if graph.is_not_empty():
                graph_labels.write(graph.get_classification()+"\n")
