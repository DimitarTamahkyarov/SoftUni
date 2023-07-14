import unittest

from project.mammal import Mammal


class MammalTest(unittest.TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Gosho", "Lion", "Roar...")

    def test_init(self):
        self.assertEqual(self.mammal.name, "Gosho")
        self.assertEqual(self.mammal.type, "Lion")
        self.assertEqual(self.mammal.sound, "Roar...")
        self.assertEqual(self.mammal._Mammal__kingdom, "animals")

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), "Gosho makes Roar...")

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), "animals")

    def test_info(self):
        self.assertEqual(self.mammal.info(), f"{self.mammal.name} is of type {self.mammal.type}")


if __name__ == '__main__':
    unittest.main()