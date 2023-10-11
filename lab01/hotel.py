import sys

rooms = {
    1: {
        'id': 1,
        'roomCapacity': 1,
    },
    2: {
        id: 2,
        'roomCapacity': 2,
    },
    3: {
        id: 3,
        'roomCapacity': 2,
    },
}

room_occupacy = {}  # defaultdict(list,{ k:[] for k in rooms.keys() })
person_room = {}


def main():
    init_room_occupacy_dict()
    for i in range(1, len(sys.argv), 2):
        if sys.argv[i] == '--stan_pokoi':
            print_room_status()
        else:
            name = sys.argv[i]
            number = int(sys.argv[i + 1])
            add_reservation(name, number)


def init_room_occupacy_dict():
    for idx in rooms:
        room_occupacy[idx] = 0


def add_reservation(name, number):
    if type(name) != str or type(number) != int:
        print("Błędny format danych")
    if room_occupacy[number] < rooms[number]['roomCapacity']:
        person_room[name] = number
        room_occupacy[number] += 1
    else:
        print(f"Błąd! {name} nie został zakwaterowany do pokoju z powodu braku miejsca")


def reverse_dict(dict):
    reversed_dict = {}
    for key, value in dict.items():
        reversed_dict[value] = []
    for key, value in dict.items():
        reversed_dict[value].append(key)
    return reversed_dict


def print_room_status():
    print("-------------+--------+")
    print("Numer pokoju | Goście |")
    print("-------------+--------+")
    dict_reversed = reverse_dict(person_room)
    for number, guests in dict_reversed.items():
        print("{}             {}".format(number, "\n              ".join(guests)))


if __name__ == "__main__":
    main()
