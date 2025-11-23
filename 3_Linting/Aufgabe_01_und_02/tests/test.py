import unittest
from src.house import House

class TestHouse(unittest.TestCase):
    def test_create(self):
        house = House()

        self.assertIsInstance(house, House)

    def test_set_name(self):
        house = House()
        house_name = "nice_house"

        house.set_name(house_name)

        self.assertEqual(house.name, house_name)

    def test_get_name(self):
        house = House()
        house.set_name("nicer_house")
       
        result = house.get_name()

        self.assertEqual(result, "nicer_house")

if __name__ == '__main__':
    unittest.main()