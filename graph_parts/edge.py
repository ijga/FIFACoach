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
    

    def create_feature_vector(self):
        # returns something in the form [int, int, float, float, int], valid feature vector
        return [self.player.id, self.target.id, self.angle, self.distance, self.type]


    def toString(self) -> str:
        return f'(Edge: {self.id} {self.angle} {self.type}; {self.player.toString()} -> {self.target.toString()})'


    def __str__(self) -> str:
        return f'(Edge: {self.id} {self.angle} {self.type}; {self.player.toString()} -> {self.target.toString()})'