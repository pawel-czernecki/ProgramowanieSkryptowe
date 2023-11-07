from model import Animal, Vector2d, MoveDirection, MapDirection
from controller import OptionsParser, Simulation
import sys

if __name__ == "__main__":
    animal = Animal(Vector2d(2, 2))
    print(animal)

    directions: list[MoveDirection] = OptionsParser.parse(sys.argv[1:])
    positions: list[Vector2d] = [Vector2d(2, 2),
                                 Vector2d(3, 4)]  # Pozycje początkowe dla zwierząt, odpowiednio, (2,2) oraz (3,4)
    simulation: Simulation = Simulation(directions, positions)

    print(directions)
    print(sys.argv[1:])

    simulation.run()

# py .\main.py f b r l f f r r f f f f f f f f