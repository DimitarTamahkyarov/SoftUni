import unittest
from project.vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(1000, 100)

    def test_init(self):
        self.assertEqual(self.vehicle.fuel, 1000)
        self.assertEqual(self.vehicle.capacity, 1000)
        self.assertEqual(self.vehicle.horse_power, 100)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_drive_method_work_correctly(self):
        self.vehicle.drive(100)
        self.assertEqual(self.vehicle.fuel, 875)
        self.vehicle.drive(700)
        self.assertEqual(self.vehicle.fuel, 0)

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1)

        self.assertEqual(str(ex.exception), "Not enough fuel")

    def test_refuel_with_too_much_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_enough_fuel(self):
        self.vehicle.fuel = 500
        self.vehicle.refuel(100)
        self.assertEqual(self.vehicle.fuel, 600)

    def test_str_method(self):
        expected_result = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

        actual_result = str(self.vehicle)

        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()