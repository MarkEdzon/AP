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
    days = int(input("\t\t[6] Enter the number of days you will stay: "))
    room_cost = 1200 if room_category == "single" else 2400
    total_cost = room_cost * days

    reservation = Reservation(name, check_in_date, check_out_date, guests, room_number, room_category, total_cost)
    reservations.append(reservation)
    print(f"Reservation added successfully! Total cost: {total_cost} pesos.")


def search_reservation(reservations):
    name = input("Enter the name for the reservation to search: ")
    for reservation in reservations:
        if reservation.name == name:
            print("Reservation found:")
            print_reservation_details(reservation)
            return
    print("Reservation not found.")

def update_reservation(reservations):
    name = input("Enter the name for the reservation to update: ")
    for reservation in reservations:
        if reservation.name == name:
            reservation.check_in_date = input("Enter new check-in date (YYYY-MM-DD): ")
            reservation.check_out_date = input("Enter new check-out date (YYYY-MM-DD): ")
            reservation.guests = int(input("Enter new number of guests: "))
            days = int(input("Enter new number of days of stay: "))
            room_cost = 1200 if reservation.room_category == "single" else 2400
            reservation.total_cost = room_cost * days
            print(f"Reservation updated successfully! New total cost: {reservation.total_cost} pesos.")
            return
    print("Reservation not found.")

def delete_reservation(reservations, available_rooms, room_categories):
    name = input("Enter the name for the reservation to delete: ")
    for reservation in reservations:
        if reservation.name == name:
            available_rooms.append(reservation.room_number)
            room_categories.append(reservation.room_category)
            reservations.remove(reservation)
            print("Reservation deleted successfully!")
            return
    print("Reservation not found.")

def display_reservations(reservations):
    if not reservations:
        print("No reservations available.")
        return
    print("All reservations:")
    for reservation in reservations:
        print_reservation_details(reservation)

def display_available_rooms(available_rooms, room_categories):
    if not available_rooms:
        print("No available rooms.")
        return
    print("Available rooms:")
    for i, room in enumerate(available_rooms):
        category = room_categories[i] if i < len(room_categories) else "Unknown Category"
        print(f"\tRoom {room} ({category})")


def check_out_reservations(reservations, available_rooms, room_categories):
    current_date = datetime.date.today().strftime("%Y-%m-%d")
    reservations[:] = [
        reservation for reservation in reservations
        if not is_date_before(reservation.check_out_date, current_date)
  ]

def is_date_before(date1, date2):
    return date1 <= date2

def print_reservation_details(reservation):
    print("========================================================================================================================================================================")
    print(f"Name: {reservation.name}")
    print(f"Check-in Date: {reservation.check_in_date}")
    print(f"Check-out Date: {reservation.check_out_date}")
    print(f"Number of Guests: {reservation.guests}")
    print(f"Room Number: {reservation.room_number}")
    print(f"Room Category: {reservation.room_category}")
    print(f"Total Cost: {reservation.total_cost} pesos")
    print("========================================================================================================================================================================")

def main():
    reservations = []
    print("========================================================================================================================================================================")
    available_rooms = [101, 102, 103, 104, 105]
    room_categories = ["single", "double", "single", "double", "single"]

    print("\t\t\t\t\t\t*******Welcome to the MEGA hotel reservation system!*******")
    print("========================================================================================================================================================================")
    print("The cost per day of stay is 1200 pesos")

while True:
        check_out_reservations(reservations, available_rooms, room_categories)
        print("\nMenu:")
        print("\t\t1. Add Reservation")
        print("\t\t2. Search Reservation")
        print("\t\t3. Update Reservation")
        print("\t\t4. Delete Reservation")
        print("\t\t5. Display All Reservations")
        print("\t\t6. Display Available Rooms")
        print("\t\t7. Exit")
        print("========================================================================================================================================================================")
        choice = int(input("\t\tChoose an option (1-7): "))
        print("========================================================================================================================================================================")

        if choice == 1:
            add_reservation(reservations, available_rooms, room_categories)
        elif choice == 2:
            search_reservation(reservations)
        elif choice == 3:
            update_reservation(reservations)
        elif choice == 4:
            delete_reservation(reservations, available_rooms, room_categories)
        elif choice == 5:
            display_reservations(reservations)
        elif choice == 6:
            display_available_rooms(available_rooms, room_categories)
        elif choice == 7:
            print("\t\tThank you for considering us. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
