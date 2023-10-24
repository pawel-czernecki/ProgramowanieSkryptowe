import pytest
from model import Vector2d

@pytest.fixture
def vector1():
    return Vector2d(1, 2)

@pytest.fixture
def vector2():
    return Vector2d(3, 4)

def test_get_x(vector1):
    assert vector1.get_x() == 1

def test_get_y(vector1):
    assert vector1.get_y() == 2

def test_str(vector1, vector2):
    assert str(vector1) == "(1,2)"
    assert str(vector2) == "(3,4)"

def test_precedes(vector1, vector2):
    assert vector1.precedes(vector2) is True
    assert vector2.precedes(vector1) is False

def test_follows(vector1, vector2):
    assert vector1.follows(vector2) is False
    assert vector2.follows(vector1) is True

def test_add(vector1, vector2):
    result = vector1.add(vector2)
    assert result.get_x() == 4
    assert result.get_y() == 6

def test_subtract(vector1, vector2):
    result = vector1.subtract(vector2)
    assert result.get_x() == -2
    assert result.get_y() == -2

def test_upperRight(vector1, vector2):
    result = vector1.upperRight(vector2)
    assert result.get_x() == 3
    assert result.get_y() == 4

def test_lowerLeft(vector1, vector2):
    result = vector1.lowerLeft(vector2)
    assert result.get_x() == 1
    assert result.get_y() == 2

def test_opposite(vector1):
    result = vector1.opposite()
    assert result.get_x() == -1
    assert result.get_y() == -2

def test_eq(vector1, vector2):
    assert vector1 == Vector2d(1, 2)
    assert vector1 != vector2