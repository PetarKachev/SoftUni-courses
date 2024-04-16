from project.toy_store import ToyStore
from unittest import TestCase, main

class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toy = ToyStore()

    def test_init_method(self):
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)

    def test_shelf_doesnt_exists_raise_error(self):

        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("U", "Exmp")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_name_is_the_same_raise_an_error(self):

        self.toy.toy_shelf["A"] = "Pesho"

        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "Pesho")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_name_is_none_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.toy.add_toy("A", "Pesho")
            self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_name_is_different_and_its_not_none(self):

        result = self.toy.add_toy("A", "Darin")
        self.assertEqual({
            "A": "Darin",
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)
        self.assertEqual(f"Toy:Darin placed successfully!", result)

    def test_removing_toy_the_shelf_doesnt_exists(self):

        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy("Q", "10t")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_removing_toy_the_name_is_different(self):

        self.toy.toy_shelf['A'] = "Pesho"
        with self.assertRaises(Exception) as ex:
            self.toy.remove_toy("A", "Darin")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_removing_toy_shelf_exists_and_name_is_different(self):

        self.toy.toy_shelf['A'] = "Pesho"
        result = self.toy.remove_toy("A", "Pesho")
        self.assertEqual({
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.toy.toy_shelf)
        self.assertEqual(f"Remove toy:Pesho successfully!", result)

if __name__ == "__main__":
    main()
