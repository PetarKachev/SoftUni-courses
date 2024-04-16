from unittest import TestCase, main
from project.robot import Robot


class TestRobot(TestCase):
    ALLOWED_CATEGORIES = ['Military', 'Education', 'Entertainment', 'Humanoids']

    def setUp(self) -> None:
        self.robot = Robot('C200', 'Military', 200, 10000)
        self.second_robot = Robot('C300', 'Education', 300, 20000)

    def test_init_method(self):
        self.assertEqual('C200', self.robot.robot_id)
        self.assertEqual('Military', self.robot.category)
        self.assertEqual(200, self.robot.available_capacity)
        self.assertEqual(10000, self.robot.price)
        self.assertEqual([], self.robot.hardware_upgrades)
        self.assertEqual([], self.robot.software_updates)

        self.assertEqual('C300', self.second_robot.robot_id)
        self.assertEqual('Education', self.second_robot.category)
        self.assertEqual(300, self.second_robot.available_capacity)
        self.assertEqual(20000, self.second_robot.price)
        self.assertEqual([], self.second_robot.hardware_upgrades)
        self.assertEqual([], self.second_robot.software_updates)

    def test_make_vategory_invalid_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = "Invalid"
        self.assertEqual(f"Category should be one of '{self.ALLOWED_CATEGORIES}'", str(ve.exception))

    def test_make_price_negative_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -50
        self.assertEqual("Price cannot be negative!", str(ve.exception))

    def test_check_if_the_component_not_in_the_list(self):
        self.robot.hardware_upgrades = ["TFC-20"]
        result = self.robot.upgrade("TFC-20", 500)
        self.assertEqual(f"Robot {self.robot.robot_id} was not upgraded.", result)

    def test_check_if_the_component_in_the_list(self):
        result = self.robot.upgrade("TFC-20", 1)
        self.assertEqual(["TFC-20"], self.robot.hardware_upgrades)
        self.assertEqual(10001.5, self.robot.price)
        self.assertEqual(f'Robot {self.robot.robot_id} was upgraded with TFC-20.', result)

    def test_update_function_return_error_first_scenario(self):
        self.robot.software_updates = [5.5]
        result = self.robot.update(1.1, 1)
        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)

    def test_update_function_return_error_second_scenario(self):
        self.robot.software_updates = [1.1]
        result = self.robot.update(1.1, 1)
        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)

    def test_update_function_return_error_third_scenario(self):
        self.robot.software_updates = [1.1]
        result = self.robot.update(5.5, 100000)
        self.assertEqual(f"Robot {self.robot.robot_id} was not updated.", result)

    def test_update_function_forth_scenario(self):
        result = self.robot.update(5.5, 50)
        self.assertEqual([5.5], self.robot.software_updates)
        self.assertEqual(150, self.robot.available_capacity)
        self.assertEqual(f'Robot {self.robot.robot_id} was updated to version 5.5.', result)

    def test_gt_method_our_price_is_bigger_than_the_other_robot_price(self):

        self.robot.price = 200000
        result = self.robot.__gt__(self.second_robot)
        self.assertEqual(f'Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {self.second_robot.robot_id}.', result)

    def test_gt_method_our_price_is_same_as_the_other_robots_price(self):

        self.robot.price = 20000
        result = self.robot.__gt__(self.second_robot)
        self.assertEqual(f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {self.second_robot.robot_id}.', result)

    def test_gt_method_our_price_is_less_than_the_other_robots_price(self):

        self.robot.price = 5000
        result = self.robot.__gt__(self.second_robot)
        self.assertEqual(f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {self.second_robot.robot_id}.', result)


if __name__ == '__main__':
    main()
