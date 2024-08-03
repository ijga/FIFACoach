import torch
from torch_geometric.data import InMemoryDataset, Data
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import time

def visualize_graph(data):
    G = nx.Graph()

    if data.y == 8:
        return 
    
    for i, (x, y, type) in enumerate(data.x):
        G.add_node(i, pos=(x, y))
    
    for i, (src, dst) in enumerate(data.edge_index.t().tolist()):
        G.add_edge(src, dst)
    
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=12)
    plt.show()


GAME = 1
ITER = 1
FOLDER = f"game{GAME}_{ITER}/"
FILE_HEADER = "FIFAGS_"

class FIFAGSDataset(InMemoryDataset):
    def __init__(self, root, transform=None, pre_transform=None):
        super(FIFAGSDataset, self).__init__(root, transform, pre_transform)
        self.data, self.slices = torch.load(self.processed_paths[0])

    @property
    def raw_file_names(self):
        return [FOLDER + FILE_HEADER + name for name in ['edge_attributes.txt', 
                                                         'edges.txt', 
                                                         'graph_indicator.txt',
                                                         'graph_labels.txt',
                                                         'node_attributes.txt']
                                                         ]

    @property
    def processed_file_names(self):
        return [f'{FOLDER}/data.pt']

    def process(self):
        edge_attributes = torch.tensor(np.loadtxt(self.raw_paths[0], delimiter=",", dtype=int, ndmin=2), dtype=torch.int)
        edges = torch.tensor(np.loadtxt(self.raw_paths[1], delimiter=",", dtype=int, ndmin=2), dtype=torch.int)
        graph_indicator = torch.tensor(np.loadtxt(self.raw_paths[2], delimiter=",", dtype=int, ndmin=1), dtype=torch.int)
        graph_labels = torch.tensor(np.loadtxt(self.raw_paths[3], delimiter=",", dtype=int, ndmin=1), dtype=torch.long)
        node_attributes = torch.tensor(np.loadtxt(self.raw_paths[4], delimiter=",", dtype=int, ndmin=2), dtype=torch.float)

        data_list = []

        unique_graphs = torch.unique(graph_indicator)
        for graph in unique_graphs:
            node_mask = graph_indicator == graph
            graph_nodes = torch.where(node_mask)[0]

            sub_x = node_attributes[graph_nodes]

            sub_edge_index, sub_edge_attr = self.get_subgraph_edges(graph_nodes, edges, edge_attributes)

            sub_y = graph_labels[graph]

            data = Data(x=sub_x, edge_index=sub_edge_index, edge_attr=sub_edge_attr, y=sub_y)
            
            # print(data)
            # visualize_graph(data)
            
            data_list.append(data)

        data, slices = self.collate(data_list)
        torch.save((data, slices), self.processed_paths[0])

    def get_subgraph_edges(self, graph_nodes, edges, edge_attributes):
        node_map = {i.item(): idx for idx, i in enumerate(graph_nodes)}
        
        src_np = edges[:, 0]
        mask = np.isin(src_np, np.array(graph_nodes))
        
        sub_edge_index = edges[mask]
        sub_edge_attr = edge_attributes[mask]

        sub_edge_index = torch.tensor([[node_map[src.item()], node_map[dst.item()]] for src, dst in sub_edge_index], dtype=torch.int).t().contiguous()
        return sub_edge_index, sub_edge_attr


root = '.'

start_time = time.time()
dataset = FIFAGSDataset(root)
end_time = time.time()

elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")
