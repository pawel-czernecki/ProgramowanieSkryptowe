"""
Autor: Stanisław Polak
Data utworzenia: 22-10-2023
Data modyfikacji: 22-10-2023
Wersja: 1.0
Opis: Testy klasy "Simulation".
"""
import pytest
from model import Vector2d, MoveDirection, MapDirection
from controller import Simulation, OptionsParser
@pytest.fixture
def simulation_for_two_animals():
    args = "f b r l f f r r f f f f f f f f".split(" ")
    directions: list[MoveDirection] = OptionsParser.parse(args)
    positions: list[Vector2d] = [Vector2d(2, 2), Vector2d(3, 4)]
    yield Simulation(directions, positions)
@pytest.fixture
def simulation_for_three_animals():
    args = "f b r l f f r r f f f f f f f".split(" ")
    directions: list[MoveDirection] = OptionsParser.parse(args)
    positions: list[Vector2d] = [Vector2d(2, 2), Vector2d(3, 4), Vector2d(0, 4)]
    yield Simulation(directions, positions)
def test_Simulation_run_for_two_animals(simulation_for_two_animals: Simulation):
    simulation_for_two_animals.run()
    assert simulation_for_two_animals.animals[0].position == Vector2d(3, 0)
    assert simulation_for_two_animals.animals[0].orientation == MapDirection.SOUTH
    assert simulation_for_two_animals.animals[1].position == Vector2d(2, 4)
    assert simulation_for_two_animals.animals[1].orientation == MapDirection.NORTH
def test_Simulation_run_for_three_animals(simulation_for_three_animals: Simulation):
    simulation_for_three_animals.run()
    animal_0 = simulation_for_three_animals.animals[0]
    animal_1 = simulation_for_three_animals.animals[1]
    animal_2 = simulation_for_three_animals.animals[2]
    assert animal_0.position == Vector2d(2, 4)
    assert animal_0.orientation == MapDirection.NORTH
    assert animal_1.position == Vector2d(4, 4)
    assert animal_1.orientation == MapDirection.EAST
    assert animal_2.position == Vector2d(4, 4)
    assert animal_2.orientation == MapDirection.EAST