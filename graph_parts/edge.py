from typing import Union, Dict
from graph_parts.ball import Ball
from graph_parts.goal import Goal
from graph_parts.player import Player


class Edge:
    def __init__(self, idx: int, angle: float, distance: float, type: int, player: Player, target: Union[Ball, Goal, Player]):
        self.id = int(idx)
        self.angle: float = angle
        self.distance: float = distance
        self.type: int = type # team to team, team to other team, team to goal, team to ball
        self.player = player # player
        self.target = target
    
    def create_feature_vector(self) -> str:
        # returns something in the form [int, int, int], valid feature vector
        return f"{int(round(self.angle, 2))}, {int(round(self.distance))}, {self.type}"
    
    def create_sparse_adj_matrix_pair(self, nodes_from_prev_graphs) -> str:
        return f"{self.player.id + nodes_from_prev_graphs}, {self.target.id + nodes_from_prev_graphs}"
    
    def create_sparse_adj_matrix_pair_remap(self, node_id_remapping: Dict[str, str]) -> str:
        return f"{node_id_remapping[self.player.id]}, {node_id_remapping[self.target.id]}"

    def toString(self) -> str:
        return f'(Edge: {self.id} {self.angle} {self.type}; {self.player.toString()} -> {self.target.toString()})'

    def __str__(self) -> str:
        return f'(Edge: {self.id} {self.angle} {self.type}; {self.player.toString()} -> {self.target.toString()})'