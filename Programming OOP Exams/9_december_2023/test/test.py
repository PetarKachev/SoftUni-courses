from unittest import TestCase, main
from collections import deque
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):

    def setUp(self) -> None:
        self.station = RailwayStation("Sofia")

    def test_init_method(self):
        self.assertEqual("Sofia", self.station.name)

    def test_name_test_if_2_symbols_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = "2"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_train_arrival_on_board(self):
        expected_deque = deque(["T2"])
        self.station.new_arrival_on_board("T2")
        self.assertEqual(expected_deque, self.station.arrival_trains)

    def test_train_has_arrived_the_info_is_the_same_as_in_the_input(self):
        self.station.arrival_trains = deque(["T2"])
        result = self.station.train_has_arrived("C50")
        self.assertEqual(f"There are other trains to arrive before C50.", result)

    def test_train_has_arrived_the_same_info_for_trains(self):
        self.station.arrival_trains = deque(["T2"])
        result = self.station.train_has_arrived("T2")
        self.assertEqual(deque(["T2"]), self.station.departure_trains)
        self.assertEqual(f"T2 is on the platform and will leave in 5 minutes.", result)

    def test_train_has_left(self):
        self.station.departure_trains = deque(["T2"])
        result = self.station.train_has_left("T2")
        expected_deque = deque()
        self.assertEqual(expected_deque, self.station.departure_trains)
        self.assertTrue(result)

    def test_train_has_left_but_different_values(self):
        self.station.departure_trains = deque(["T2"])
        result = self.station.train_has_left("C2")
        self.assertFalse(result)

if __name__ == "__main__":
    main()
