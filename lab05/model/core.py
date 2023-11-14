from enum import Enum
from typing import Tuple

class Vector2d:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return f"({self.x},{self.y})"

    def precedes(self, other_Vector2d):
        return self.x <= other_Vector2d.get_x() and self.y <= other_Vector2d.get_y()

    def follows(self, other_Vector2d):
        return self.x >= other_Vector2d.get_x() and self.y >= other_Vector2d.get_y()

    def add(self, other_Vector2d):
        new_x = self.x + other_Vector2d.get_x()
        new_y = self.y + other_Vector2d.get_y()
        return Vector2d(new_x, new_y)

    def subtract(self, other_Vector2d):
        new_x = self.x - other_Vector2d.get_x()
        new_y = self.y - other_Vector2d.get_y()
        return Vector2d(new_x, new_y)

    def __add__(self, other: 'Vector2d') -> 'Vector2d':
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vector2d') -> 'Vector2d':
        return Vector2d(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if isinstance(other, Vector2d):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))

class MoveDirection(Enum):
    FORWARD = "f"
    BACKWARD = "b"
    RIGHT = "r"
    LEFT = "l"

    def toUnitVector(self) -> Vector2d:
        if self == MoveDirection.FORWARD:
            return Vector2d(0, 1)
        elif self == MoveDirection.BACKWARD:
            return Vector2d(0, -1)
        elif self == MoveDirection.RIGHT:
            return Vector2d(1, 0)
        elif self == MoveDirection.LEFT:
            return Vector2d(-1, 0)

class MapDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __str__(self) -> str:
        directions = ["↑", "→", "↓", "←"]
        return directions[self.value]

    def next(self) -> 'MapDirection':
        return MapDirection((self.value + 1) % 4)

    def previous(self) -> 'MapDirection':
        return MapDirection((self.value - 1) % 4)

    def toUnitVector(self) -> Vector2d:
        if self == MapDirection.NORTH:
            return Vector2d(0, 1)
        elif self == MapDirection.EAST:
            return Vector2d(1, 0)
        elif self == MapDirection.SOUTH:
            return Vector2d(0, -1)
        elif self == MapDirection.WEST:
            return Vector2d(-1, 0)