import pytest
import skrypt

move_description = skrypt.moves_dictionary

def test_run_valid_moves():
    moves = ["f", "b", "l", "r"]
    result = skrypt.run(moves, move_description)

    assert result == ["Zwierzak idzie do przodu", "Zwierzak idzie do tyłu", "Zwierzak skręca w lewo", "Zwierzak skręca w prawo"]

def test_run_invalid_moves():
    moves = ["f", "b", "l", "x", "l"]

    result = skrypt.run(moves, move_description)
    assert result == ["Zwierzak idzie do przodu","Zwierzak idzie do tyłu","Zwierzak skręca w lewo","Zwierzak skręca w lewo"]

def test_run_empty_moves():
    moves = []

    result = skrypt.run(moves, move_description)
    assert result == []

# Przypadek testowy 1: Sprawdź, czy funkcja poprawnie wyświetla argumenty bez indeksów
def test_display_without_index(capsys):
    args = ["foo", "bar", "test"]
    show_index = False
    skrypt.display(args, show_index)
    captured = capsys.readouterr()
    expected_output = "foo\nbar\ntest\n"
    assert captured.out == expected_output

# Przypadek testowy 2: Sprawdź, czy funkcja poprawnie wyświetla argumenty z indeksami
def test_display_with_index(capsys):
    args = ["foo", "bar", "test"]
    show_index = True
    skrypt.display(args, show_index)
    captured = capsys.readouterr()
    expected_output = "args[0] = foo\nargs[1] = bar\nargs[2] = test\n"
    assert captured.out == expected_output

# Przypadek testowy 3: Sprawdź, czy funkcja działa poprawnie dla pustej listy argumentów
def test_display_empty_list(capsys):
    args = []
    show_index = False
    skrypt.display(args, show_index)
    captured = capsys.readouterr()
    expected_output = ""
    assert captured.out == expected_output