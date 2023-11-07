class Vector2d:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def __str__(self):
        return f"({self.__x},{self.__y})"
    def precedes(self, other_Vector2d):
        return self.__x <= other_Vector2d.get_x() and self.__y <= other_Vector2d.get_y()
    def follows(self, other_Vector2d):
        return self.__x >= other_Vector2d.get_x() and self.__y >= other_Vector2d.get_y()
    def add(self, other_Vector2d):
        new_x = self.__x + other_Vector2d.get_x()
        new_y = self.__y + other_Vector2d.get_y()
        return Vector2d(new_x, new_y)
    def subtract(self, other_Vector2d):
        new_x = self.__x - other_Vector2d.get_x()
        new_y = self.__y - other_Vector2d.get_y()
        return Vector2d(new_x, new_y)
    def upperRight(self, other_Vector2d):
        new_x = max(self.__x, other_Vector2d.get_x())
        new_y = max(self.__y, other_Vector2d.get_y())
        return Vector2d(new_x, new_y)
    def lowerLeft(self, other_Vector2d):
        new_x = min(self.__x, other_Vector2d.get_x())
        new_y = min(self.__y, other_Vector2d.get_y())
        return Vector2d(new_x, new_y)
    def opposite(self):
        new_x = -self.__x
        new_y = -self.__y
        return Vector2d(new_x, new_y)
    def __eq__(self, other_Vector2d):
        return self.__x == other_Vector2d.get_x() and self.__y == other_Vector2d.get_y()

'''
    position1 = Vector2d(1, 2)
    print(position1)  # (1,2)
    position2 = Vector2d(-2, 1)
    print(position2)  # (-2,1)
    print(position1.add(position2))  # (-1,3)
    print(position1.subtract(position2))  # (3,1)
    print(position1.lowerLeft(position2))  # (-2,1)
    print(position1.upperRight(position2))  # (1,2)
    print(position1.precedes(position2))  # False
    print(position1.follows(position2))  # True
    print(position1.opposite())  # (-1,-2)
    print(position1.__eq__(position2))  # False
'''

from enum import Enum

class MoveDirection(Enum):
    FORWARD = "f"
    BACKWARD = "b"
    LEFT = "l"
    RIGHT = "r"

class MapDirection(Enum):
    NORTH = Vector2d(0, 1)
    EAST = Vector2d(1, 0)
    SOUTH = Vector2d(0, -1)
    WEST = Vector2d(-1, 0)

    def __str__(self):
        if self == MapDirection.EAST:
            return "→"
        elif self == MapDirection.WEST:
            return "←"
        elif self == MapDirection.NORTH:
            return "↑"
        elif self == MapDirection.SOUTH:
            return "↓"

    def next(self):
        if self == MapDirection.EAST:
            return MapDirection.SOUTH
        elif self == MapDirection.SOUTH:
            return MapDirection.WEST
        elif self == MapDirection.WEST:
            return MapDirection.NORTH
        elif self == MapDirection.NORTH:
            return MapDirection.EAST

    def previous(self):
        if self == MapDirection.EAST:
            return MapDirection.NORTH
        elif self == MapDirection.NORTH:
            return MapDirection.WEST
        elif self == MapDirection.WEST:
            return MapDirection.SOUTH
        elif self == MapDirection.SOUTH:
            return MapDirection.EAST

    def toUnitVector(self):
        return self.value

class Animal:
    def __init__(self, position: Vector2d, orientation: MapDirection = MapDirection.NORTH):
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
        return f"{self.position} {self.orientation}"

    def __repr__(self) -> str:
        return str(self)

    def isAt(self, position: Vector2d) -> bool:
        return self.position == position

    def move(self, direction: MoveDirection) -> None:
        if direction == MoveDirection.RIGHT or direction == MoveDirection.LEFT:
            self.orientation = self.get_new_orientation(direction)
        elif direction == MoveDirection.FORWARD or direction == MoveDirection.BACKWARD:
            new_position = self.get_new_position(direction)
            if self.isWithinMapBounds(new_position):
                self.position = new_position

    def get_new_orientation(self, direction: MoveDirection) -> MapDirection:
        if direction == MoveDirection.RIGHT:
            return self.orientation.next()
        elif direction == MoveDirection.LEFT:
            return self.orientation.previous()

    def get_new_position(self, direction: MoveDirection) -> Vector2d:
        if direction == MoveDirection.FORWARD:
            return self.position.add(self.orientation.toUnitVector())
        elif direction == MoveDirection.BACKWARD:
            return self.position.subtract(self.orientation.toUnitVector())

    def isWithinMapBounds(self, position: Vector2d) -> bool:
        map_bounds = (Vector2d(0, 0), Vector2d(4, 4))
        return map_bounds[0].precedes(position) and map_bounds[1].follows(position)


if __name__ == "__main__":
    print(MapDirection.EAST)  # →
    print(MapDirection.EAST.next())  # ↓
    print(MapDirection.EAST.previous())  # ↑
    print(MapDirection.EAST.toUnitVector())  # (1,0)