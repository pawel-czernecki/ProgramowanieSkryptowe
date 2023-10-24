from controller import OptionsParser
from model import MoveDirection

def test_parse_valid_args():
    args = ["f", "b", "l", "r"]
    parsed_args = OptionsParser.parse(args)
    expected_result = [MoveDirection.f.value, MoveDirection.b.value, MoveDirection.l.value, MoveDirection.r.value]
    assert parsed_args == expected_result

def test_parse_invalid_args():
    args = ["f", "x", "r", "z"]
    parsed_args = OptionsParser.parse(args)
    expected_result = [MoveDirection.f.value, MoveDirection.r.value]
    assert parsed_args == expected_result

def test_parse_empty_args():
    args = []
    parsed_args = OptionsParser.parse(args)
    expected_result = []
    assert parsed_args == expected_result

def test_parse_mixed_args():
    args = ["f", "b", "x", "r", "l", "z"]
    parsed_args = OptionsParser.parse(args)
    expected_result = [MoveDirection.f.value, MoveDirection.b.value, MoveDirection.r.value, MoveDirection.l.value]
    assert parsed_args == expected_result