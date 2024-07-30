from classification_maps import game_object_classification_names


class GameObject:
    def __init__(self, idx: int, x: float, y: float, type: int):
        self.id = idx
        self.x = x
        self.y = y
        self.type = type


    def create_feature_vector(self):
        # returns something in the form [int, float, float, int], valid feature vector
        return [self.id, self.x, self.y, self.type]


    def __eq__(self, other) -> bool:
        return self.id == other.id and self.x == other.x and self.y == other.y and self.type == other.type


    def toString(self) -> str:
        return f'- {self.id} {game_object_classification_names[self.type]} :({self.x}, {self.y})-'


    def __str__(self) -> str:
        return f'- {self.id} {game_object_classification_names[self.type]} :({self.x}, {self.y})-'