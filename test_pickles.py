import pickle
from graph import Graph

GAME = "1"

with open(f"unlabeled_graphs/game{GAME}.pickle", "rb") as unlabeled:
    with open(f"labeled_graphs/game{GAME}.pickle", "rb") as labeled:
        for i in range(650):
            unlabeled_graph: Graph = pickle.load(unlabeled)
            labeled_graph: Graph = pickle.load(labeled)

            print(f"{i}, {unlabeled_graph == labeled_graph}, {unlabeled_graph.attacking_classification}, {labeled_graph.attacking_classification}")
            x = unlabeled_graph.man_city.values()
            print(*x)
            y = labeled_graph.man_city.values()
            print(*y)
            print('------')
            x = unlabeled_graph.man_city_gk
            print(*x)
            y = labeled_graph.man_city_gk
            print(*y)
            print('------')
            x = unlabeled_graph.man_utd.values()
            print(*x)
            y = labeled_graph.man_utd.values()
            print(*y)
            print('------')
            x = unlabeled_graph.man_utd_gk
            print(*x)
            y = labeled_graph.man_utd_gk
            print(*y)
            print('------')
            x = unlabeled_graph.ball
            print(*x)
            y = labeled_graph.ball
            print(*y)
            print('------')
            print('===========')