from model.core import Vector2d, MoveDirection
from model.interface import IMoveValidator, IWorldMap
from model.animal import Animal
from view import MapVisualizer
from model.positionException import PositionAlreadyOccupiedError

class WorldMap(IMoveValidator, IWorldMap):
    def __init__(self):
        self.animals = {}

    def isPositionOccupied(self, position: Vector2d) -> bool:
        return position in self.animals

    def place(self, animal):
        if not self.isPositionOccupied(animal.position) and self.isInsideMap(animal.position):
            self.animals[animal.position] = animal
        else:
            raise PositionAlreadyOccupiedError(animal.position)

    def removeAnimal(self, animal) -> None:
        if animal.position in self.animals:
            del self.animals[animal.position]

    def canMoveTo(self, position: Vector2d) -> bool:
        return self.isInsideMap(position) and not self.isPositionOccupied(position)

    def isOccupied(self, position: Vector2d) -> bool:
        return self.isPositionOccupied(position)

    def objectAt(self, position: Vector2d):
        return self.animals.get(position, None)
    
    def move(self, animal: Animal, direction: MoveDirection) -> None:
        new_position = animal.position

        if direction == MoveDirection.FORWARD:
            new_position += animal.orientation.toUnitVector()
        elif direction == MoveDirection.BACKWARD:
            new_position -= animal.orientation.toUnitVector()
        if direction == MoveDirection.RIGHT:
            new_position += animal.orientation.toUnitVector()
        elif direction == MoveDirection.LEFT:
            new_position -= animal.orientation.toUnitVector()

        if self.canMoveTo(new_position):
            self.removeAnimal(animal)
            animal.move(direction, self)
            self.place(animal)

    def __str__(self) -> str:
        visualizer = MapVisualizer(self)
        return visualizer.draw(self.lowerLeft, self.upperRight)
    
class RectangularMap(WorldMap, IMoveValidator, IWorldMap):
    def __init__(self, width: int, height: int):
        super().__init__()
        self.width = width
        self.height = height
        self.upperRight = Vector2d(self.width,self.height)
        self.lowerLeft = Vector2d(0,0)

    def isInsideMap(self, position: Vector2d) -> bool:
        return 0 <= position.x <= self.width and 0 <= position.y <= self.height

class InfiniteMap(WorldMap, IMoveValidator, IWorldMap):
    def __init__(self):
        super().__init__()
        self.animals = {}
        self.upperRight = Vector2d(0, 0)
        self.lowerLeft = Vector2d(0, 0)
        self.setNewBounds()
    def isInsideMap(self, position: Vector2d) -> bool:
        return True

    def setNewBounds(self) -> None:
        if len(self.animals) == 0:
            return

        min_x = min(animal.position.x for animal in self.animals.values())
        min_y = min(animal.position.y for animal in self.animals.values())
        self.lowerLeft = Vector2d(min_x, min_y)

        max_x = max(animal.position.x for animal in self.animals.values())
        max_y = max(animal.position.y for animal in self.animals.values())
        self.upperRight = Vector2d(max_x, max_y)


    def __str__(self) -> str:
        self.setNewBounds()
        return super().__str__()