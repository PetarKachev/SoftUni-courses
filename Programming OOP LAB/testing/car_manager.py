from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self) -> None:
        self.car = Car("Mercedes", "C200", 20, 70)

    def test_init_func(self):
        self.assertEqual("Mercedes", self.car.make)
        self.assertEqual("C200", self.car.model)
        self.assertEqual(20, self.car.fuel_consumption)
        self.assertEqual(70, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_func(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_func(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_func(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_method(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_changing_values(self):
        expected_fuel = self.car.fuel_amount + 2
        self.car.refuel(2)
        self.assertEqual(expected_fuel, self.car.fuel_amount)

    def test_driving_values_change(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(500000)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_driving(self):
        expected_fuel_amount = self.car.fuel_amount - (-1 / 100) * self.car.fuel_consumption
        self.car.drive(-1)
        self.assertEqual(expected_fuel_amount, self.car.fuel_amount)

if __name__ == "__main__":
    main()