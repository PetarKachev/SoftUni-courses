from unittest import TestCase, main


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker("Brian", 1500, 100)

    def test_checking_the_init(self):
        self.assertEqual("Brian", self.worker.name)
        self.assertEqual(1500, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.money = -100

    def test_check_the_money_and_the_energy(self):
        expected_money = self.worker.salary
        expected_energy = self.worker.energy - 1

        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_exception_error_handling(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_rest_command(self):
        expected_energy = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_command(self):
        expected_command = f'{self.worker.name} has saved {self.worker.money} money.'

        self.worker.get_info()

        self.assertEqual(expected_command, self.worker.get_info())


if __name__ == "__main__":
    main()
