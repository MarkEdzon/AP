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