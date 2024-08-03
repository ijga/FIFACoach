# Use dataset in a DataLoader
from torch_geometric.loader import DataLoader
from p4_save_pytorch_datasets import FIFAGSDataset  # Import the data module
import matplotlib.pyplot as plt
import networkx as nx

ROOT = '.'

dataset = FIFAGSDataset(ROOT)

train_loader = DataLoader(dataset, batch_size=2, shuffle=True)

# Print loaded data
for data in train_loader:
    print(data)
    for graph in data.to_data_list():
        print(graph, graph.y[0].item())




# # Usage
# dataset = MyDataset(root='path/to/dataset')


# train_loader = DataLoader(dataset, batch_size=32, shuffle=True)


# class GCN(torch.nn.Module):
#     def __init__(self, num_node_features, hidden_channels):
#         super(GCN, self).__init__()
#         self.conv1 = GCNConv(num_node_features, hidden_channels)
#         self.conv2 = GCNConv(hidden_channels, hidden_channels)
#         self.lin = torch.nn.Linear(hidden_channels, 1)  # Binary classification

#     def forward(self, data):
#         x, edge_index, batch = data.x, data.edge_index, data.batch
#         x = self.conv1(x, edge_index)
#         x = F.relu(x)
#         x = self.conv2(x, edge_index)
#         x = global_mean_pool(x, batch)  # [batch_size, hidden_channels]
#         x = self.lin(x)
#         return x

# model = GCN(num_node_features=1, hidden_channels=16)

# optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

# def train():
#     model.train()
#     for data in train_loader:
#         optimizer.zero_grad()
#         out = model(data)
#         loss = F.binary_cross_entropy_with_logits(out, data.y.float().unsqueeze(1))
#         loss.backward()
#         optimizer.step()

# for epoch in range(1, 201):
#     train()
