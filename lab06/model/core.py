from enum import Enum
from typing import Tuple

import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        qualified_name = f"{func.__qualname__}"
        argument_values = ', '.join(map(repr, args))
        print(f"    Nazwa kwalifikowana: {qualified_name}")
        print(f"    Argumenty: {argument_values}")
        result = func(*args, **kwargs)
        return result
    return wrapper

def log_to(file):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            qualified_name = f"{func.__qualname__}"
            argument_values = ', '.join(map(repr, args))
            log_entry = f"{qualified_name} | {argument_values}"

            with open(f"{file}.txt", 'a') as log_file:
                log_file.write(log_entry + '\n')

            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

class Vector2d:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @log
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

    @log_to("dziennik")
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

    def __repr__(self):
        return f"({self.x},{self.y})"

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

    def __add__(self, other):
        if isinstance(other, int):
            return MapDirection((self.value + other) % 4)
        else:
            raise TypeError("Can't add MapDirection with other type than int")

    def toUnitVector(self) -> Vector2d:
        if self == MapDirection.NORTH:
            return Vector2d(0, 1)
        elif self == MapDirection.EAST:
            return Vector2d(1, 0)
        elif self == MapDirection.SOUTH:
            return Vector2d(0, -1)
        elif self == MapDirection.WEST:
            return Vector2d(-1, 0)

'''

py -i model/core.py  
v1 = Vector2d(1,2)
v2=v1.add(Vector2d(1,1))
v2.get_x()

'''