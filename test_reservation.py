import unittest
from hotel_reservation import Reservation, add_reservation


class TestReservationSystem(unittest.TestCase):
    def test_add_reservation(self):
        reservations = []
        available_rooms = [101, 102, 103, 104, 105]
        room_categories = ["single", "double", "single", "double", "single"]

        test_name = "Mark"
        mock_inputs = [
            test_name,
            "2024-12-01",
            "2024-12-05",
            "1",
            "101",
            "4"
        ]

        room_number = int(mock_inputs[4])
        room_index = available_rooms.index(room_number)
        room_category = room_categories[room_index]
        room_rate = 1200 if room_category == "single" else 2400

        inputs = iter(mock_inputs)

        def mock_input(prompt):
            return next(inputs)

        global input
        original_input = input
        input = mock_input

        try:
            add_reservation(reservations, available_rooms, room_categories)
        finally:
            input = original_input

        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0].name, test_name)
        self.assertEqual(reservations[0].room_number, room_number)
        self.assertEqual(reservations[0].total_cost, room_rate * int(mock_inputs[5]))
        self.assertNotIn(room_number, available_rooms)


if __name__ == '__main__':
    unittest.main()
