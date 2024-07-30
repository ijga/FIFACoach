from graph_parts.game_object import GameObject


class Player(GameObject):
    def __init__(self, idx: int, x, y, type):
        super().__init__(idx, x, y, type)
