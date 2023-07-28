import unittest
from unittest import main
from project.truck_driver import TruckDriver


class TruckDriverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("driver", 100)

    def test__init__(self):
        self.assertEqual(self.driver.name, "driver")
        self.assertEqual(self.driver.money_per_mile, 100)
        assert isinstance(self.driver.available_cargos, dict)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_setter_with_invalid_value(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual(str(ve.exception), "driver went bankrupt.")

    def test_earned_money_setter_with_valid_value(self):
        self.driver.earned_money = 10

        self.assertEqual(self.driver.earned_money, 10)

    def test_add_cargo_offer_with_invalid_value(self):
        self.driver.available_cargos["Varna"] = 1000

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Varna", 100)

        self.assertEqual(str(ex.exception), "Cargo offer is already added.")

    def test_add_cargo_offer_with_valid_value(self):
        res = self.driver.add_cargo_offer("Burgas", 100)

        assert res == "Cargo for 100 to Burgas was added as an offer."
        self.assertEqual(self.driver.available_cargos["Burgas"], 100)

    def test_drive_best_cargo_offer_with_invalid_value(self):
        res = self.driver.drive_best_cargo_offer()

        self.assertEqual(res, "There are no offers available.")

    def test_drive_best_cargo_offer_with_valid_value(self):
        self.driver.available_cargos = {"Burgas": 100, "Varna": 250, "Ruse": 50}
        res = self.driver.drive_best_cargo_offer()

        self.assertEqual(res, "driver is driving 250 to Varna.")
        self.assertEqual(self.driver.earned_money, 24980)
        self.assertEqual(self.driver.miles, 250)

    def test_check_for_activities(self):
        self.driver.earned_money = 50_000
        self.driver.check_for_activities(10_000)

        self.assertEqual(self.driver.earned_money, 38_250)

    def test_eat(self):
        self.driver.earned_money = 20
        self.driver.eat(250)

        assert self.driver.earned_money == 0

    def test_sleep(self):
        self.driver.earned_money = 45
        self.driver.sleep(1000)

        assert self.driver.earned_money == 0

    def test_pump_gas(self):
        self.driver.earned_money = 500
        self.driver.pump_gas(1500)

        assert self.driver.earned_money == 0

    def test_repair_truck(self):
        self.driver.earned_money = 7500
        self.driver.repair_truck(10000)

        assert self.driver.earned_money == 0




    def test__repr__(self):
        self.assertEqual(str(self.driver), "driver has 0 miles behind his back.")


if __name__ == "__main__":
    main()
