import operations
import sys

text = sys.argv[1]

print(operations.first_character(text))
print(operations.first_two_characters(text))
print(operations.all_characters_except_first_two(text))
print(operations.penultimate_character(text))
print(operations.last_three_characters(text))
print(operations.all_characters_in_even_positions(text))
print(operations.merge_characters_and_duplicate(text))