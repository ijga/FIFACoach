from typing import Union
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
        # returns something in the form float, float, int], valid feature vector
        return f"{round(self.angle, 2)}, {round(self.distance, 2)}, {self.type}"
    
    def create_sparse_adj_matrix_pair(self) -> str:
        return f"{self.player.id}, {self.target.id}"

    def toString(self) -> str:
        return f'(Edge: {self.id} {self.angle} {self.type}; {self.player.toString()} -> {self.target.toString()})'

    def __str__(self) -> str:
        return f'(Edge: {self.id} {self.angle} {self.type}; {self.player.toString()} -> {self.target.toString()})'