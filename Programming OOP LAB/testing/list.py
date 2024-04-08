from unittest import TestCase, main

class TestIntegerList(TestCase):

    def setUp(self) -> None:

        self.list = IntegerList(5.5, 1, 2, 3, 4.5)

    def test_init(self):

        self.assertEqual([1, 2, 3], self.list.get_data())

    def test_add_method_the_type_if_its_integer(self):

        with self.assertRaises(ValueError) as ex:
            self.list.add(5.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_if_the_command_will_add_an_element_to_the_list(self):

        self.list.get_data() + [4]
        self.list.add(4)
        self.assertEqual([1, 2, 3, 4], self.list.get_data())

    def test_removing_index_exception_message(self):

        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(1000)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_removing_an_element_on_a_specific_index(self):

        self.list.remove_index(2)
        self.assertEqual([1, 2], self.list.get_data())

    def test_get_element_on_a_specific_index(self):

        with self.assertRaises(IndexError) as ex:
            self.list.get(1000)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_getting_on_a_specific_element(self):

        self.list.get(2)
        self.assertEqual(3, self.list.get(2))

    def test_insert_an_element_exception_handle(self):

        with self.assertRaises(IndexError) as ex:
            self.list.insert(1000, 5)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_an_element_exception_handle_2(self):

        with self.assertRaises(ValueError) as ex:
            self.list.insert(2, "Example")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_inserting_an_element_properly(self):

        self.list.insert(0, 5)
        self.assertEqual([5, 1, 2, 3], self.list.get_data())

    def test_getting_biggest_num(self):

        self.list.get_biggest()
        self.assertEqual(3, self.list.get_biggest())

    def test_get_index(self):

        self.list.get_index(3)
        self.assertEqual(2, self.list.get_index(3))


if __name__ == "__main__":
    main()
