from typing import List
from time import sleep
from model.interface import IWorldMap
from model.core import MoveDirection, Vector2d
from model.animal import Animal
from model.positionException import PositionAlreadyOccupiedError
class Simulation:
    def __init__(self, directions: List[MoveDirection], positions: List[Vector2d], world_map: IWorldMap):
        self.directions = directions
        self.map = world_map
        self.animals = []
        for position in positions:
            try:
                self.map.place(Animal(position))
            except PositionAlreadyOccupiedError as e:
                print(e)
                break
            self.animals.append(Animal(position))

    def run(self):
        num_animals = len(self.animals)
        current_animal_index = 0

        for direction in self.directions:
            print(self.map)

            current_animal = self.animals[current_animal_index]
            self.map.move(current_animal, direction)
            print(f"Zwierzę {current_animal_index}: {current_animal}")

            current_animal_index = (current_animal_index + 1) % num_animals

            sleep(1)



class OptionsParser:

    @staticmethod
    def map_to_direction(arg):
        legal_moves = {direction.value: direction for direction in MoveDirection}
        if arg in legal_moves:
            return legal_moves[arg]
        else:
            raise ValueError(f"{arg} is not a legal move specification")
    @staticmethod
    def parse(args: List[str]) -> List[MoveDirection]:
        return list(map(OptionsParser.map_to_direction, args))
