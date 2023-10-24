import sys
from controller import OptionsParser

def display(args):
    for arg in args:
        print(arg)

print("System wystartował.")
move_list = OptionsParser.parse(sys.argv[1:])

display(move_list)
print("System zakończył działanie.")