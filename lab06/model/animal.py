from model.core import MapDirection, MoveDirection, Vector2d
from model.interface import IMoveValidator
from typing import Callable

class Animal:
    def __init__(self, position: Vector2d, orientation: MapDirection = MapDirection.NORTH):
        self.position = position
        self.orientation = orientation

    def __str__(self) -> str:
        return str(self.orientation)

    def isAt(self, position: Vector2d) -> bool:
        return self.position == position

    def move(self, direction: MoveDirection, validator: IMoveValidator) -> None:
        update_fn = self._get_update_function(direction, validator)
        update_fn(self)

    def _get_update_function(self, direction: MoveDirection, validator: IMoveValidator) -> Callable[['Animal'], None]:
        update_map = {
            MoveDirection.RIGHT: lambda obj: setattr(obj, 'orientation', obj.orientation + 1),
            MoveDirection.LEFT: lambda obj: setattr(obj, 'orientation', obj.orientation + (-1)),
            MoveDirection.FORWARD: lambda obj: setattr(obj, 'position', obj.position + obj.orientation.toUnitVector()) if validator.canMoveTo(obj.position + obj.orientation.toUnitVector()) else obj,
            MoveDirection.BACKWARD: lambda obj: setattr(obj, 'position', obj.position - obj.orientation.toUnitVector()) if validator.canMoveTo(obj.position - obj.orientation.toUnitVector()) else obj
        }
        return update_map.get(direction, lambda obj: obj)

    def __repr__(self) -> str:
        return str(self.orientation)