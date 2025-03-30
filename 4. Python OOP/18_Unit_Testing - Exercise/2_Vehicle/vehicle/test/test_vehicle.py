from unittest import TestCase, main

from project.vehicle import Vehicle

if __name__ == '__main__':
    main()

class TestVehicle(TestCase):
    fuel = 45.5
    horse_power = 125.5

    def setUp(self):
        self.vehicle = Vehicle(self.fuel, self.horse_power)

    def test_class_attributes_types(self):
        self.assertIsInstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float)
        self.assertIsInstance(self.vehicle.fuel_consumption, float)
        self.assertIsInstance(self.vehicle.fuel, float)
        self.assertIsInstance(self.vehicle.capacity, float)
        self.assertIsInstance(self.vehicle.horse_power, float)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.fuel, self.vehicle.capacity)
        self.assertEqual(self.horse_power, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_success(self):
        self.vehicle.drive(20)
        self.assertEqual(20.5, self.vehicle.fuel)

    def test_drive_error_raises(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(3000)
        self.assertEqual("Not enough fuel", str(ex.exception))
        self.assertEqual(self.fuel, self.vehicle.fuel)

    def test_refuel_success(self):
        self.vehicle.fuel = 1
        self.vehicle.refuel(30.5)
        self.assertEqual(31.5, self.vehicle.fuel)

    def test_refuel_failure_raises(self):
        self.vehicle.fuel = 40
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(30)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        expected = f"The vehicle has {self.horse_power} horse power with {self.fuel} fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.vehicle))
