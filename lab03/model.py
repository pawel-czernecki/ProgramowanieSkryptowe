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
    f = "Zwierzak idzie do przodu"
    b = "Zwierzak idzie do tyłu"
    l = "Zwierzak skręca w lewo"
    r = "Zwierzak skręca w prawo"