import argparse
import json
import re
import sys

def importJsonFile(file):
    with open(file, 'r') as f:
        data = json.load(f)
        return data
def main():
    main_parser = argparse.ArgumentParser(prog="hotel.py", description="Skrypt 3 - REALIZUJe funkcjonalność skryptu 1 i 2")
    main_parser.add_argument("file", help="Plik zawierający informację o pokojach")

    data = importJsonFile(main_parser.parse_args().file)

    if not data:
        print("Nie znaleziono pliku")
        return

    for line in sys.stdin:
        lines_arg = line.removesuffix('\n').split(' ')
        if lines_arg[0] == "rooms":
            print_room_status(data)
        elif lines_arg[0] == "book":
            for reservation in lines_arg[1:]:
                reservation_data = get_reservation_data_from_string(reservation)
                for single_reservation in reservation_data:
                    add_reservation(single_reservation["name"], single_reservation["room_number"], single_reservation["date"], data)
        elif lines_arg[0] == "show":
            guestList = lines_arg[1].split(',')
            show(data, guestList)
        else:
            print("Nieznana komenda")

def show(data, names):

    for name in names:
        print('\n')
        print(name)
        print("---------------------+------------")
        print("{:<20} | {:<12}".format("Termin", "Numer pokoju"))
        print("---------------------+------------")
        for room_id, room_data in data.items():
            for reservation in room_data['roomReservation']:
                if reservation['name'] == name:
                    print("{:<20} | {:<12}".format(reservation['date'], room_id))

def get_reservation_data_from_string(string):
    result = []

    if string=="":
        return result

    splited_guest_list = string.split('|', 1)

    if len(splited_guest_list) != 2:
        print("Błędny format danych")
        return result

    geust_name = splited_guest_list[0]
    reservations = splited_guest_list[1].split(':')
    for single_reservation in reservations:
        room_number = re.findall(r'\(.*?\)', single_reservation)
        date = re.sub(r'\([^)]+\)', '', single_reservation)

        if len(room_number) != 1:
            print("Błędny format danych (konwersja numeru pokoju)")
            continue

        room_number = room_number[0]
        room_number = room_number.replace('(', '').replace(')', '')

        if room_number == "":
            print("Błędny format danych (brak numeru pokoju)")
            continue

        result.append({
            "name": geust_name,
            "room_number": int(room_number),
            "date": date
        })

    return result
def add_reservation(name, number, term, data):
    if type(name) != str or type(number) != int or type(term) != str:
        print("Błędny format danych (nie udało skonwertować się danych do rezerwacji)")

    if data.get(str(number)) is None:
        print("Pokój nie istnieje")
        return

    if len(data[str(number)]['roomReservation']) < data[str(number)]['roomCapacity']:
        data[str(number)]['roomReservation'].append({
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
