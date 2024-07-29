from pynput import keyboard
import pickle
import cv2
from graph import Graph

GAME = "1"
ITER = "1"

with open(f"labeled_graphs/game{GAME}_{ITER}.pickle", "rb") as labeled:
    with open(f"vectorized_graphs/game{GAME}_{ITER}.pickle", "wb") as vectorized:

                
        graph: Graph = pickle.load(labeled)

        # do hella transformations


        pickle.dump(graph, vectorized)

