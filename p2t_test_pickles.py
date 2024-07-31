import pickle
from graph import Graph

GAME = "1"
ITER = "1"

with open(f"unlabeled_graphs/game{GAME}.pickle", "rb") as unlabeled:
    with open(f"labeled_graphs/game{GAME}_{ITER}.pickle", "rb") as labeled:
        for i in range(650):
            unlabeled_graph: Graph = pickle.load(unlabeled)
            labeled_graph: Graph = pickle.load(labeled)

            print(labeled_graph)

            print(f"{i}, {unlabeled_graph == labeled_graph}, {unlabeled_graph.attacking_classification}, {labeled_graph.attacking_classification}")
            