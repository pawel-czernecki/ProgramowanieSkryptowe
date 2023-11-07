from model import MoveDirection, Animal, Vector2d, MapDirection

class OptionsParser:
    @staticmethod
    def parse(args):
        parsed_args = []

        for arg in args:
            if arg in [item.value for item in MoveDirection]:
                parsed_args.append(arg)

        return parsed_args


class Simulation:
    def __init__(self, directions: list[MoveDirection], positions: list[Vector2d]) -> None:
        self.directions = directions
        self.animals = [Animal(position) for position in positions]

    def run(self) -> None:
        num_animals = len(self.animals)
        for move_direction in self.directions:
            for i in range(num_animals):
                animal = self.animals[i]
                animal.move(move_direction)
                print(f'Zwierzę {i}: ({animal.position.get_x()},{animal.position.get_y()}) {animal.orientation}')