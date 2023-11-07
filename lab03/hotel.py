from datetime import datetime, date
import sys
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
    def __init__(self, name):
        self.name = name
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
    def __init__(self, room, guest, start, end):
        self.guest = guest
        self.room = room
        self.start = start
        self.end = end

list_of_rooms = [
    Room(1, 1, 150),
    Room(2, 3, 250),
    Room(3, 2, 200)
]

list_of_guests = [
    Guest("Jan Kowalski"),
    Guest("Anna Kowalska"),
    Guest("Joanna Bielecka")
]

#list_of_guests[0].book(list_of_rooms[1], datetimedate(2024, 1, 1), datetimedate(2024, 1, 30))
#list_of_guests[0].book(list_of_rooms[1], datetimedate(2024, 2, 14), datetimedate(2024, 2, 27))

print(list_of_guests[0])

room1 = list_of_rooms[1]
room2 = list_of_rooms[2]
print(room1)
print(room2)

print(list_of_guests)

def main():
    for line in sys.stdin:
        lines_arg = line.removesuffix('\n').split(' ')
        if lines_arg[0] == "rooms":
            print(list_of_rooms)
        elif lines_arg[0] == "guest":
            if len(lines_arg)>=2:
                print(list_of_guests[int(lines_arg[1])])
            else:
                print(list_of_guests)
        elif lines_arg[0] == "book":
            list_of_guests[int(lines_arg[1])].book(list_of_rooms[int(lines_arg[2])], datetime.strptime(lines_arg[3], "%Y-%m-%d"), datetime.strptime(lines_arg[4],"%Y-%m-%d"))
        else:
            print("Nieznana komenda")

if __name__ == "__main__":
    main()