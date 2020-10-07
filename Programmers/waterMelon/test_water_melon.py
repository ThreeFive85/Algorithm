import unittest
import water_melon


class TestWaterMelon(unittest.TestCase):

    def test_water_melon1(self):
        result = water_melon.solution(3)
        self.assertEqual(result, "수박수")

    def test_water_melon2(self):
        result = water_melon.solution(4)
        self.assertEqual(result, "수박수박")

    def test_water_melon3(self):
        result = water_melon.solution(1)
        self.assertEqual(result, "수")


if __name__ == '__main__':
    unittest.main()
