import sys

def display(args, show_index):
    for i, arg in enumerate(args):
        print( f"args[{i}] = {arg}" if show_index else arg)

moves_dictionary = {
    "f":"Zwierzak idzie do przodu",
    "b":"Zwierzak idzie do tyłu",
    "l":"Zwierzak skręca w lewo",
    "r":"Zwierzak skręca w prawo"
}

def run(moves, move_description):
    result = []
    for move in moves:
        if move in ["f", "b", "l", "r"]:
            result.append(move_description[move])
    return result
    

print("System wystartował.")
moves_result = run(sys.argv, moves_dictionary)
display(moves_result, show_index=False)
print("System zakończył działanie.")