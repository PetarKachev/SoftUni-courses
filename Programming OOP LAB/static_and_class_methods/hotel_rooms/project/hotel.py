from project.room import Room


class Hotel:

    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")


    def add_room(self, room: Room):

        if room not in self.rooms:
            self.rooms.append(room)

    def take_room(self, room_number, people):

        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
            if room:
                if room.capacity >= people:
                    room.is_taken = True
                    room.guests += people
                    self.guests += people
        except StopIteration:
            pass

    def free_room(self, room_number):

        try:
            room = next(filter(lambda r: r.number == room_number, self.rooms))
            if room:
                room.is_taken = False
                self.guests -= room.guests
                room.guests = 0
        except StopIteration:
            pass

    def status(self):
        info = f"Hotel {self.name} has {self.guests} total guests\n"
        info += f"Free rooms: {', '.join(str(room.number) for room in self.rooms if room.is_taken == False)}\n"
        info += f"Taken rooms: {', '.join(str(room.number) for room in self.rooms if room.is_taken == True)}\n"
        return info


from project.hotel import Hotel
from project.room import Room
import unittest


class Tests(unittest.TestCase):
    def setUp(self):
        self.room = Room(1, 3)
        self.hotel = Hotel("Some Hotel")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.room.number, 1)
        self.assertEqual(self.room.capacity, 3)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(self.room.is_taken, False)

    def test_take_room_success(self):
        self.room.take_room(2)
        self.assertEqual(self.room.is_taken, True)
        self.assertEqual(self.room.guests, 2)

    def test_take_room_not_enough_capacity(self):
        result = self.room.take_room(4)
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(result, "Room number 1 cannot be taken")

    def test_take_room_not_free(self):
        self.room.take_room(1)
        result = self.room.take_room(1)
        self.assertEqual(self.room.is_taken, True)
        self.assertEqual(self.room.guests, 1)
        self.assertEqual(result, "Room number 1 cannot be taken")

    def test_free_room_success(self):
        self.room.take_room(1)
        self.room.free_room()
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)

    def test_free_room_not_taken(self):
        result = self.room.free_room()
        self.assertEqual(self.room.is_taken, False)
        self.assertEqual(self.room.guests, 0)
        self.assertEqual(result, "Room number 1 is not taken")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.hotel.name, "Some Hotel")
        self.assertEqual(self.hotel.rooms, [])
        self.assertEqual(self.hotel.guests, 0)

    def test_class_methods_creates_a_hotel(self):
        hotel = Hotel.from_stars(3)
        self.assertEqual(hotel.name, "3 stars Hotel")
        self.assertEqual(self.hotel.rooms, [])
        self.assertEqual(self.hotel.guests, 0)

    def test_add_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.assertEqual(self.hotel.rooms, [room])

    def test_take_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        self.assertEqual(self.hotel.rooms[0].is_taken, True)

    def test_free_room(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        self.hotel.free_room(1)
        self.assertEqual(self.hotel.guests, 0)
        self.assertEqual(self.hotel.rooms[0].is_taken, False)
        self.assertEqual(self.hotel.rooms[0].guests, 0)

    def test_print_status(self):
        room = Room(1, 3)
        self.hotel.add_room(room)
        self.hotel.take_room(1, 3)
        res = self.hotel.status().strip()
        actual = 'Hotel Some Hotel has 3 total guests\nFree rooms: \nTaken rooms: 1'
        self.assertEqual(res, actual)


if __name__ == "__main__":
    unittest.main()