from unittest import TestCase, main

from project.mammal import Mammal

if __name__ == "__main__":
    main()

class TestMammal(TestCase):
    def setUp(self):
        self.mammal = Mammal("Lion", "Asian", "Roaring")


    def test_init(self):
        self.assertEqual("Lion", self.mammal.name)
        self.assertEqual("Asian", self.mammal.type)
        self.assertEqual("Roaring", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Lion makes Roaring", result)

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual("Lion is of type Asian", result)