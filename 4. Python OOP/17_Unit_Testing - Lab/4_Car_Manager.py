class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)


from unittest import TestCase, main


class TestCar(TestCase):
    def setUp(self):
        self.car = Car("test", "testov", 10, 50)

    def test_init(self):
        self.assertEqual("test", self.car.make)
        self.assertEqual("testov", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_setter_empty_value_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
            self.car.make = None
            self.car.make = []

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_set_model_empty_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
            self.car.model = None
            self.car.model = []

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_zero_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
            self.car.fuel_capacity = -1

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_less_than_zero_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_zero_or_less_raises(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
            self.car.refuel(-1)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel(self):
        self.assertEqual(0, self.car.fuel_amount)

        self.car.refuel(10)

        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_above_capacity(self):
        self.assertEqual(0, self.car.fuel_amount)

        self.assertEqual(50, self.car.fuel_capacity)

        self.car.refuel(60)

        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_exact_amount_drives(self):
        needed = 10
        self.car.fuel_amount = 10

        self.car.drive(100)

        self.assertEqual(0, self.car.fuel_amount)

    def test_drive_left_amount_fuel(self):
        self.car.fuel_amount = 11

        self.car.drive(100)

        self.assertEqual(1, self.car.fuel_amount)

    def test_drive_not_enough_fuel(self):
        self.car.fuel_amount = 1
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    main()
