import math
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from typing import Dict, List

from graph_parts import Ball, Edge, Goal, Player
from classification_maps import game_object_classification_names, edge_classification_ids


def euclidean_distance(player, target) -> float:
    x1, y1 = player.x, player.y
    x2, y2 = target.x, target.y
    distance: float = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance


def angle_to(player, target) -> float:
    x1, y1 = player.x, player.y
    x2, y2 = target.x, target.y

    # Calculate the differences in coordinates
    dx = x2 - x1
    dy = y2 - y1
    
    # Calculate the angle using arctan
    angle_rad = math.atan2(dy, dx)
    
    # Convert angle from radians to degrees
    angle_deg = math.degrees(angle_rad)
    
    # Ensure the angle is positive (between 0 and 360 degrees)
    if angle_deg < 0:
        angle_deg += 360
    
    return angle_deg


class Graph:
    """ A graph that represents the on-screen game state
    
    This is a bidirectional graph where an edge represents the distance and angle that the destination has in relation to the souce

    Attacking Classifications:
        1: Best scoring opportunity: shoot the ball now!
        2: Good scoring opportunity: A few dribbles or a short pass to get a great shot off. Maybe a shot is good here
        3: Ok scoring opportunity: A long pass or a few short passes to get a good shot off. 
           If the circumstances are perfect, a shot may be good here
        4: Minor scoring threat potentially with a long ball
        5: Possession is in attacking half, no scoring threat
        6: Possession in own half
        7: Man City is defending
        8: Ignored for whatever reason (cutscene, etc)
    
    """
    def __init__(self):
        self.man_city = {}
        self.man_city_gk = []
        self.man_utd = {}
        self.man_utd_gk = []
        self.goal = []
        self.ball = []
        self.edges = defaultdict(list)
        # attacking_classification: scale of 1-7 where 1 is a clear scoring opportunity, 5 is the worst attacking situation, 
        #                           6 is possession of ball in your own half, 7 is defending (ignored), 8 is ignored
        self.attacking_classification: int = None


    def clear(self):
        self.man_city: Dict[int, Player] = {}
        self.man_city_gk: List[Player] = []
        self.man_utd: Dict[int, Player] = {}
        self.man_utd_gk: List[Player] = []
        self.goal: List[Goal] = []
        self.ball: List[Ball] = []
        self.edges: dict[int, List[Edge]] = defaultdict(list)
        self.attacking_classification: int = None


    def add_classification(self, classification: int):
        self.attacking_classification = classification


    def add_player(self, player):
        print(player)
        if game_object_classification_names[player.type] == 'man_city':
            self.man_city[player.id] = player
        elif game_object_classification_names[player.type] == 'man_utd':
            self.man_utd[player.id] = player


    def add_gk(self, player):
        if game_object_classification_names[player.type] == 'man_city_gk':
            self.man_city_gk = [player]
        elif game_object_classification_names[player.type] == 'man_utd_utd':
            self.man_utd_gk = [player]


    def add_goal(self, goal):
        if self.goal:
            if goal.type == self.goal[0].type:
                if game_object_classification_names[goal.type] == "right_goal":
                    pass
                elif game_object_classification_names[goal.type] == "left_goal":
                    pass
        else:
            self.goal = [goal]
            

    def add_ball(self, ball):
        self.ball = [ball]


    def add_edges(self, degree):
        self.edges = defaultdict(list)  # resets edges
        idx = 0

        for player in self.man_city.values():  # edges between each of the players, going both ways
            for target in self.man_city.values():
                if player.id != target.id:
                    angle = angle_to(player, target)
                    distance = euclidean_distance(player, target)
                    self.edges[player.id].append(Edge(idx, angle, distance, edge_classification_ids['team'], player, target))
                    idx += 1

        for player in self.man_city.values():  # edges between each man_city player and "degree" closest man_utd players
            distances = []

            for target in self.man_utd.values():
                distance = euclidean_distance(player, target)
                distances.append((distance, target))

            sorted_distances = sorted(distances, key=lambda x: x[0])
            # print(sorted_distances)

            for i in range(min(degree, len(sorted_distances))):
                distance, target = sorted_distances[i]
                angle = angle_to(player, target)
                self.edges[player.id].append(Edge(idx, angle, distance, edge_classification_ids['opponent'], player, target))
                idx += 1

        if self.ball:
            distances = []
            ball = self.ball[0]

            for player in self.man_city.values():  # find closest man_city player to ba;;
                distance = euclidean_distance(player, ball)
                distances.append((distance, player))

            sorted_distances = sorted(distances, key=lambda x: x[0])

            distance, player = sorted_distances[0]
            angle = angle_to(player, ball)
            self.edges[player.id].append(Edge(idx, angle, distance, edge_classification_ids['ball'], player, ball))
            idx += 1

        if self.man_utd_gk:  # encode goalkeeper and goal into graph
            if self.goal:
                distances = []
                goal = self.goal[0]

                for player in self.man_city:  # find "degree" closest players to goal
                    distance = euclidean_distance(player, goal)
                    distances.append((distance, player))

                sorted_distances = sorted(distances, key=lambda x: x[0])
                
                for i in range(min(degree, len(sorted_distances))):
                    distance, player = sorted_distances[i]
                    angle = angle_to(player, goal)
                    self.edges[player.id].append(Edge(idx, angle, edge_classification_ids['goal'], player, goal))
                    idx += 1


    def visualize_graph(self):
        G = nx.Graph()

        city = {player.id: (player.x, -1 * player.y) for player in self.man_city.values()}
        utd = {player.id: (player.x, -1 * player.y) for player in self.man_utd.values()}
        ball = {ball.id: (ball.x, -1 * ball.y) for ball in self.ball}
        game_objects = {**city, **utd, **ball}
        if self.man_city_gk:
            gk = self.man_city_gk[0]
            game_objects.update({gk.id: (gk.x, -1 * gk.y)})
        elif self.man_utd_gk:
            gk = self.man_utd_gk[0]
            game_objects.update({gk.id: (gk.x, -1 * gk.y)})

        for vertex in game_objects:
            G.add_node(vertex)

        for src, edges in self.edges.items():
            for edge in edges:
                G.add_edge(src, edge.target.id)

        fig, ax = plt.subplots()
        pos = game_objects
        nx.draw(G, pos=pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=12)
        plt.show()
        # plt.close(fig)


    def __str__(self) -> str:
        return "game_state"
    

    def __eq__(self, other) -> bool:        
        return ([(id, player.toString()) for id, player in self.man_city.items()] == [(id, player.toString()) for id, player in other.man_city.items()] 
                and [player.toString() for player in self.man_city_gk] == [player.toString() for player in other.man_city_gk]
                and [(id, player.toString()) for id, player in self.man_utd.items()] == [(id, player.toString()) for id, player in other.man_utd.items()]
                and [player.toString() for player in self.man_utd_gk] == [player.toString() for player in other.man_utd_gk]
                and [ball.toString() for ball in self.ball] == [ball.toString() for ball in other.ball])
