from graph_parts.game_object import GameObject


class Ball(GameObject):
    def __init__(self, id, x, y, type):
        super().__init__(id, x, y, type)
