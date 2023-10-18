import argparse
import json
import sys

def importJsonFile(file):
    with open(file, 'r') as f:
        data = json.load(f)
        return data
def main():
    main_parser = argparse.ArgumentParser(prog="hotel.py", description="Skrypt 3 - REALIZUJe funkcjonalność skryptu 1 i 2")
    main_parser.add_argument("file", help="Plik zawierający informację o pokojach")

    data = importJsonFile(main_parser.parse_args().file)

    for line in sys.stdin:
        lines_arg = line.removesuffix('\n').split(' ')
        if lines_arg[0] == "room":
            print("Wyświetalnie pokoi")
            print_room_status(data)

def add_reservation(name, number, term, data):
    if type(name) != str or type(number) != int or type(term) != str:
        print("Błędny format danych")
    if len(data[number].roomReservation) < data[number].roomCapacity:
        data[number].roomReservation.append({
            "name": name,
            "date": term
        })
    else:
        print(f"Błąd! {name} nie został zakwaterowany do pokoju z powodu braku miejsca")

def print_room_status(data):
    print("-------------+------------------------+-----------+")
    print("Numer pokoju | Goście                 |  Terminy   ")
    print("-------------+------------------------+-----------+")
    for room_id, room_data in data.items():
        room_number = str(room_id)

        count = 1
        is_first = True

        for reservation in room_data['roomReservation']:
            if not is_first:
                room_number = " "

            print(f"{room_number.rjust(13)} | {count}.{reservation['name'].rjust(18)} | {count}.{reservation['date'].rjust(9)}")
            count += 1
            is_first = False

        while count <= room_data['roomCapacity']:
            if not is_first:
                room_number = " "

            print(f"{room_number.rjust(13)} | {str(count).rjust(18)}. | {str(count).rjust(6)}.")
            count += 1
            is_first = False

if __name__ == "__main__":
    main()
