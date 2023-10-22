import hotel
import json
import tempfile
import os
def test_get_reservation_data_from_string_valid_format():
    string = "Jan_Kowalski|01.11.2023-03.11.2023(1):31.12.2023-02.01.2024(2)"
    expected_result = [
        {"name": "Jan_Kowalski", "room_number": 1, "date": "01.11.2023-03.11.2023"},
        {"name": "Jan_Kowalski", "room_number": 2, "date": "31.12.2023-02.01.2024"}
    ]
    assert hotel.get_reservation_data_from_string(string) == expected_result

# Test przypadku braku pokoju w nawiasach
def test_get_reservation_data_from_string_missing_room():
    string = "Jan_Kowalski|01.11.2023-03.11.2023():31.12.2023-02.01.2024(2)"
    expected_result = [
        {"name": "Jan_Kowalski", "room_number": 2, "date": "31.12.2023-02.01.2024"},
    ]
    assert hotel.get_reservation_data_from_string(string) == expected_result

# Test przypadku błędnego formatu danych (brak znaku '|')
def test_get_reservation_data_from_string_invalid_format():
    string = "Jan_Kowalski01.11.2023-03.11.2023(1):31.12.2023-02.01.2024(2)"
    assert hotel.get_reservation_data_from_string(string) == []

def test_get_reservation_data_from_string_empty_string():
    string = ""
    assert hotel.get_reservation_data_from_string(string) == []

def test_add_reservation_room_not_exists(capsys):
    data = {
        '101': {'roomReservation': [{'name': 'Janina_Kowalska', 'date': '01.11.2023-03.11.2023'}], 'roomCapacity': 1},
        '102': {'roomReservation': [], 'roomCapacity': 2}
    }
    name = "Jan_Kowalski"
    number = 104
    term = "01.11.2023-03.11.2023"
    hotel.add_reservation(name, number, term, data)
    captured = capsys.readouterr()
    expected_output = "Pokój nie istnieje\n"
    assert captured.out == expected_output

def test_add_reservation_valid_reservation(capsys):
    data = {
        '101': {'roomReservation': [], 'roomCapacity': 2},
        '102': {'roomReservation': [], 'roomCapacity': 1}
    }
    name = "Jan_Kowalski"
    number = 101
    term = "01.11.2023-03.11.2023"
    hotel.add_reservation(name, number, term, data)
    captured = capsys.readouterr()
    assert captured.out == ""
    assert len(data['101']['roomReservation']) == 1

def test_add_reservation_no_room_capacity(capsys):
    data = {
        '101': {'roomReservation': [{'name': 'Janina_Kowalska', 'date': '01.11.2023-03.11.2023'}], 'roomCapacity': 1},
        '102': {'roomReservation': [], 'roomCapacity': 2}
    }
    name = "Jan_Kowalski"
    number = 101
    term = "01.11.2023-03.11.2023"
    hotel.add_reservation(name, number, term, data)
    captured = capsys.readouterr()
    expected_output = "Błąd! Jan_Kowalski nie został zakwaterowany do pokoju z powodu braku miejsca\n"
    assert captured.out == expected_output
    assert len(data['101']['roomReservation']) == 1

sample_json_data = {
        "test": "test",
        "test2": "test2",
        "test3": {
            "test4": "test4",
            "test5": "test5",
        },
    }

def test_importJsonFile():
    with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
        json.dump(sample_json_data, temp_file)
        temp_file_name = temp_file.name

    loaded_data = hotel.importJsonFile(temp_file_name)

    assert loaded_data == sample_json_data

    os.remove(temp_file_name)