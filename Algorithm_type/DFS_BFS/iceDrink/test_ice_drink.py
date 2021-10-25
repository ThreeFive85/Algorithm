import unittest
import ice_drink


class TestIceDrink(unittest.TestCase):

    def test_ice_drink1(self):
        element1 = [[0, 0, 1, 1, 0], [0, 0, 0, 1, 1],
                    [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]]
        result = ice_drink.solution(element1)
        self.assertEqual(result, 3)

    def test_ice_drink2(self):
        element1 = [[0, 1, 0, 1, 0, 1]]
        result = ice_drink.solution(element1)
        self.assertEqual(result, 3)

    def test_ice_drink3(self):
        element1 = [[0, 0, 0, 0, 0, 0]]
        result = ice_drink.solution(element1)
        self.assertEqual(result, 1)

    def test_ice_drink4(self):
        element1 = [[0, 0], [1, 1], [0, 0]]
        result = ice_drink.solution(element1)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
