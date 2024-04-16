from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "Metal", 100, 100)

    def test_init_method(self):
        self.assertEqual("Mountain", self.robot.category)
        self.assertEqual("Metal", self.robot.part_type)
        self.assertEqual(100, self.robot.capacity)
        self.assertEqual(100, self.robot.memory)
        self.assertEqual([], self.robot.installed_software)

    def test_category_if_its_the_good(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "Invalid"
        self.assertEqual(f"Category should be one of {self.ALLOWED_CATEGORIES}", str(ex.exception))

    def test_used_capacity(self):
        self.robot.installed_software = [{"name": "JavaScript", "capacity_consumption": 30, "memory_consumption": 50},
                                         {"name": "Python", "capacity_consumption": 30, "memory_consumption": 50}]

        result = self.robot.get_used_capacity()
        self.assertEqual(60, result)

    def test_available_capacity(self):
        self.robot.installed_software = [{"name": "JavaScript", "capacity_consumption": 30, "memory_consumption": 50},
                                         {"name": "Python", "capacity_consumption": 30, "memory_consumption": 50}]

        result = self.robot.get_available_capacity()
        self.assertEqual(40, result)

    def test_used_memory(self):
        self.robot.installed_software = [{"name": "JavaScript", "capacity_consumption": 30, "memory_consumption": 40},
                                         {"name": "Python", "capacity_consumption": 30, "memory_consumption": 40}]

        result = self.robot.get_used_memory()
        self.assertEqual(80, result)

    def test_available_memory(self):
        self.robot.installed_software = [{"name": "JavaScript", "capacity_consumption": 30, "memory_consumption": 40},
                                         {"name": "Python", "capacity_consumption": 30, "memory_consumption": 40}]

        result = self.robot.get_available_memory()
        self.assertEqual(20, result)

    def test_install_software_method(self):
        self.robot.installed_software = [{"name": "JavaScript", "capacity_consumption": 10, "memory_consumption": 10},
                                         {"name": "Python", "capacity_consumption": 10, "memory_consumption": 10}]

        expected_installed_software = [{"name": "JavaScript", "capacity_consumption": 10, "memory_consumption": 10},
                                       {"name": "Python", "capacity_consumption": 10, "memory_consumption": 10},
                                       {"name": "JavaScript", "capacity_consumption": 10, "memory_consumption": 10}]

        result = self.robot.install_software({"name": "JavaScript", "capacity_consumption": 10, "memory_consumption": 10})
        self.assertEqual(expected_installed_software, self.robot.installed_software)
        self.assertEqual(f"Software 'JavaScript' successfully installed on {self.robot.category} part.", result)



    def test_install_software_if_everything_is_with_same_value(self):
        self.robot.installed_software = [{"name": "JavaScript", "capacity_consumption": 10, "memory_consumption": 10},
                                         {"name": "Python", "capacity_consumption": 10, "memory_consumption": 10}]

        expected_installed_software = [{"name": "JavaScript", "capacity_consumption": 10, "memory_consumption": 10},
                                       {"name": "Python", "capacity_consumption": 10, "memory_consumption": 10},
                                       {"name": "JavaScript", "capacity_consumption": 80, "memory_consumption": 80}]

        result = self.robot.install_software({"name": "JavaScript", "capacity_consumption": 80, "memory_consumption": 80})
        self.assertEqual(expected_installed_software, self.robot.installed_software)
        self.assertEqual(f"Software 'JavaScript' successfully installed on {self.robot.category} part.", result)

    def test_install_software_fail(self):
        self.robot.installed_software = [{"name": "JavaScript", "capacity_consumption": 10, "memory_consumption": 10},
                                         {"name": "Python", "capacity_consumption": 10, "memory_consumption": 10}]

        result = self.robot.install_software({"name": "JavaScript", "capacity_consumption": 200, "memory_consumption": 200})
        expected_message = f"Software 'JavaScript' cannot be installed on {self.robot.category} part."
        self.assertEqual(expected_message, result)

    def test_install_software_fail_first_part(self):
        self.robot.installed_software = [{"name": "JavaScript", "capacity_consumption": 10, "memory_consumption": 10},
                                         {"name": "Python", "capacity_consumption": 10, "memory_consumption": 10}]

        result = self.robot.install_software({"name": "JavaScript", "capacity_consumption": 200, "memory_consumption": 20})
        expected_message = f"Software 'JavaScript' cannot be installed on {self.robot.category} part."
        self.assertEqual(expected_message, result)

    def test_install_software_fail_second_part(self):
        self.robot.installed_software = [{"name": "JavaScript", "capacity_consumption": 10, "memory_consumption": 10},
                                         {"name": "Python", "capacity_consumption": 10, "memory_consumption": 10}]

        result = self.robot.install_software({"name": "JavaScript", "capacity_consumption": 20, "memory_consumption": 200})
        expected_message = f"Software 'JavaScript' cannot be installed on {self.robot.category} part."
        self.assertEqual(expected_message, result)

if __name__ == "__main__":
    main()
