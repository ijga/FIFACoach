import pickle
from graph_parts import Graph
import torch
from torch_geometric.data import InMemoryDataset, download_url

GAME = "1"
ITER = "1"
FRAMES = 54120
VID_STRIDE=90
PICKLE_LENGTH = FRAMES//VID_STRIDE

with open(f"labeled_graphs/game{GAME}_{ITER}.pickle", "rb") as labeled:
    with open(f"vectorized_graphs/game{GAME}_{ITER}.pickle", "wb") as vectorized:
        for i in range(PICKLE_LENGTH):
                
            graph: Graph = pickle.load(labeled)
            print(graph)

            # do hella transformations


            pickle.dump(graph, vectorized)

class GameStates(InMemoryDataset):
    pass