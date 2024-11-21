import datetime

class Reservation:
    def __init__(self, name, check_in_date, check_out_date, guests, room_number, room_category, total_cost):
        self.name = name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.guests = guests
        self.room_number = room_number
        self.room_category = room_category
        self.total_cost = total_cost


def add_reservation(reservations, available_rooms, room_categories):
    if not available_rooms:
        print("Sorry, no rooms are available.")
        return
    print("========================================================================================================================================================================")
    name = input("\t\t[1] Please enter your name: ")
    check_in_date = input("\t\t[2] Enter check-in date (YYYY-MM-DD): ")
    check_out_date = input("\t\t[3] Enter check-out date (YYYY-MM-DD): ")
    guests = int(input("\t\t[4] Enter the number of guests: "))
    
    print("\t\t[5] Available rooms:")
    for i, room in enumerate(available_rooms):
        print(f"\t\tRoom {room} ({room_categories[i]})")
    room_number = int(input("\n\t\tChoose a room number: "))

    if room_number in available_rooms:
        index = available_rooms.index(room_number)
        room_category = room_categories[index]
        del available_rooms[index]
        del room_categories[index]
   else:
        print("Invalid room number. Reservation not added.")
        return
