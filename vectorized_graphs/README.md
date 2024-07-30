README for dataset FIFAGS (FIFA Game State)

=== Usage ===

This folder contains the following comma separated text files:

n = total number of nodes
m = total number of edges
N = number of graphs

(1) FIFAGS_edges.txt (m lines)
sparse (block diagonal) adjacency matrix for all graphs,
each line corresponds to (row, col) resp. (node_id, node_id)

(2) FIFAGS_graph_indicator.txt (n lines)
column vector of graph identifiers for all nodes of all graphs,
the value in the i-th line is the graph_id of the node with node_id i

(3) FIFAGS_graph_labels.txt (N lines)
class labels for all graphs in the dataset,
the value in the i-th line is the class label of the graph with graph_id i

(6) FIFAGS_edge_attributes.txt (m lines; same size as FIFAGS_A.txt)
attributes for the edges in FIFAGS_A.txt

(7) FIFAGS_node_attributes.txt (n lines)
matrix of node attributes,
the comma seperated values in the i-th line is the attribute vector of the node with node_id i

=== Description of the dataset ===

Placeholder

Graph labels:

1 - Best scoring opportunity: shoot the ball now!
2 - Good scoring opportunity: A few dribbles or a short pass to get a great shot off. Maybe a shot is good here
3 - Ok scoring opportunity: A long pass or a few short passes to get a good shot off. If the circumstances are perfect, a shot may be good here
4 - Minor scoring threat potentially with a long ball
5 - Possession is in attacking half, no scoring threat
6 - Possession in own half
7 - Man City is defending
8 - Ignored for whatever reason (cutscene, etc)

Node Attributes:

\\# int - id of node

\\# float - x position of node

\\# float - y position of node

0 - ball
3 - left_goal
4 - man_city (player)
5 - man_city_gk
6 - man_utd (player)
7 - man_utd_dk
9 - right_goal

Edge Attributes

\\# float - angle of edge wrt player

\\# float - length of edge

0 - player to teammate
1 - player to opponent
2 - player to ball
3 - player to goal
