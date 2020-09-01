import unittest
import coins


class TestCoins(unittest.TestCase):

    def test_coins1(self):
        result = coins.solution(1260)
        self.assertEqual(result, 6)

    def test_coins2(self):
        result = coins.solution(800)
        self.assertEqual(result, 4)

    def test_coins3(self):
        result = coins.solution(1000)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
