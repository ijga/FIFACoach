# FIFACoach

The goal of this project is to create a ML pipeline that recommends next moves to FIFA players.

It works by having a supervised ML model that can identify the attacking threat of a game state, and a unsupervised ML model that embeds game states in a multidimensional space where more similar game states are close together. 

The pipeline will recommend a game state that is better (using the supervised ML model) than and similar to (using the unsupervised ML model) the user's current game state.

I am currently working on building the supervised ML model.

The code pipeline is broken down into files labeled p{step_number}_{function}.py/ipynb in this repository. Currently the pipeline is as follows:
1. p1_create_graph.py -> Create graph classes from screen recorded video of FIFA23 games.
   - graph.py contains the graph class
2. p2_label_graphs.py -> Read graphs from pickle file and manually label the attacking classification of graphs
3. p3_graph_vectorization.py -> Write labeled graphs into .txt files in the form of the vectors needed for homogeneous graph creation in PyTorch
4. p4_save_pytorch_datasets -> Put vectorized data into a PyTorch Geometric object and save it to a .pt file
5. p5_train_model.ipynb -> Use graphs to train a classification model that can predict the attacking classification of a game_state
