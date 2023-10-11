import unittest
import skrypt
from io import StringIO
from unittest.mock import patch


class TestRun(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_without_index(self, stdout):
        args = ["foo", "bar", "test"]
        show_index = False
        skrypt.display(args, show_index)
        expected_output = "foo\nbar\ntest\n"
        self.assertEqual(stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_with_index(self, stdout):
        args = ["foo", "bar", "test"]
        show_index = True
        skrypt.display(args, show_index)
        expected_output = "args[0] = foo\nargs[1] = bar\nargs[2] = test\n"
        self.assertEqual(stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_display_empty_list(self, stdout):
        args = []
        show_index = False
        skrypt. display(args, show_index)
        expected_output = ""
        self.assertEqual(stdout.getvalue(), expected_output)

    def test_run_valid_moves(self):
        moves = ["f", "b", "l", "r"]
        move_description = skrypt.moves_dictionary
        result = skrypt.run(moves, move_description)
        self.assertEqual(result, ["Zwierzak idzie do przodu", "Zwierzak idzie do tyłu", "Zwierzak skręca w lewo", "Zwierzak skręca w prawo"])

    def test_run_invalid_moves(self):
        moves = ["f", "b", "l", "x", "l"]
        move_description = skrypt.moves_dictionary
        result = skrypt.run(moves, move_description)
        self.assertEqual(result, ["Zwierzak idzie do przodu","Zwierzak idzie do tyłu","Zwierzak skręca w lewo","Zwierzak skręca w lewo"])


    def test_run_empty_moves(self):
        moves = []
        move_description = skrypt.moves_dictionary
        result = skrypt.run(moves, move_description)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()