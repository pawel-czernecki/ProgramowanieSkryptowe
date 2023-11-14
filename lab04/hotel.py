from datetime import datetime, date
import sys
from typing import Final
class Room:
    def __init__(self, number, capacity, price):
        self.number = number
        self.capacity = capacity
        self.price = price
        self.bookings = []

    def __str__(self):
        guest_info = "\nGoście:\n"
        current_guests = 0
        today = datetime.today()
        for booking in self.bookings:
            guest_info += f"        {booking.guest.name}   {booking.start}    {booking.end}\n"
            if booking.start <= today <= booking.end:
                print(booking, today)
                current_guests = current_guests + 1
        return f"Numer: {self.number}\nMaksymalna liczba osób: {self.capacity}\nAktualna liczba osób: {current_guests}\nCena: {self.price}\n{guest_info}"

    def __repr__(self):
        guest_info = "\nGoście:\n"
        current_guests = 0
        today = datetime.today()
        print(self.bookings)
        for booking in self.bookings:
            if booking.start <= today <= booking.end:
                current_guests = current_guests + 1
        return f"nr: {self.number} Aktualna liczba osób: {current_guests}"

class Guest:
    def __init__(self, name, pesel):
        self.name = name
        self.pesel = pesel
        self.bookings = []

    def book(self, room, check_in_date, check_out_date):
        booking = Booking(room, self, check_in_date, check_out_date)

        room.bookings.append(booking)
        self.bookings.append(booking)
    def __str__(self):
        booking_info = ""
        for booking in self.bookings:
            booking_info += f"Pokój nr {booking.room.number} {booking.start}     {booking.end}\nDo zapłaty: {booking.room.price} złotych\n"

        return f"{self.name}\n{booking_info}"
    def __repr__(self):
        return self.name

class Booking:
    def __init__(self, room: Room, guest: Guest, start: datetime.date, end: datetime.date):
        self.guest = guest
        self.room = room
        self.start = start
        self.end = end

class Hotel:
    rooms: Final = [
        Room(1, 1, 150),
        Room(2, 3, 250),
        Room(3, 2, 200),
        Room(4, 2, 200),
        Room(5, 3, 280)
    ]

    guests = [
        Guest("Jan Kowalski", "12345678901"),
        Guest("Anna Kowalska", "12345678902"),
        Guest("Joanna Bielecka", "12345678903"),
    ]

    def __init__(self):
        self.reservations = []


    def reserve_room(self, pesel, name, room, check_in_date, check_out_date):
        guest = next((g for g in self.guests if g.pesel == pesel), None)
        if not guest:
            guest = Guest(name, pesel)
            self.guests.append(guest)
            print("Zapisano nowego klienta do bazy danych")
        else:
            print("Gość istaniał już w naszej bazie danych")

        self.reservations.append(Booking(room, guest, check_in_date, check_out_date))
        print(f"Rezerwacja zrealizowana:\n{guest}\n{room}\nTermin: {check_in_date} - {check_out_date}")

    def display_guest_reservations(self, pesel):
        guest = next((g for g in self.guests if g.pesel == pesel), None)
        if guest:
            print(f"Rezerwacje dla gościa {guest}:")
            for reservation in [reservation for reservation in self.reservations if reservation.guest == guest]:
                print(f"Pokój {reservation.room.number}, {reservation.start} - {reservation.end}")
        else:
            print(f"Brak gościa o numerze PESEL {pesel}")

    def display_reservations_in_date_range(self, start_date, end_date):
        print(f"Rezerwacje w okresie {start_date} - {end_date}:")
        for reservation in self.reservations:
            if start_date <= reservation.start <= end_date or start_date <= reservation.end <= end_date:
                print(f"{reservation.guest} - Pokój {reservation.room.number} - Cena {reservation.room.price} złotych , {reservation.start} - {reservation.end}")

def main():
    hotel = Hotel()

    for line in sys.stdin:
        lines_arg = line.removesuffix('\n').split(' ')
        if lines_arg[0] == "rooms":
            print(hotel.rooms)
        elif lines_arg[0] == "guest":
            if len(lines_arg)>=2:
                print(hotel.guests[int(lines_arg[1])])
            else:
                print(hotel.guests)
        elif lines_arg[0] == "book":
            hotel.reserve_room(lines_arg[4], lines_arg[5],hotel.rooms[int(lines_arg[1])], datetime.strptime(lines_arg[2], "%Y-%m-%d"), datetime.strptime(lines_arg[3],"%Y-%m-%d"))
        elif lines_arg[0] == "pesel":
            hotel.display_guest_reservations(lines_arg[1])
        elif lines_arg[0] == "date":
            hotel.display_reservations_in_date_range(datetime.strptime(lines_arg[1], "%Y-%m-%d"), datetime.strptime(lines_arg[2],"%Y-%m-%d"))

        else:
            print("Nieznana komenda")

if __name__ == "__main__":
    main()

# book 1 2021-05-01 2021-05-10 12345678901 Jan Kowalski
# book 1 2021-05-01 2021-05-10 12345678954 Aneta Nowak
# pesel 12345678901
# date 2021-04-01 2021-05-15
