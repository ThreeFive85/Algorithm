import unittest
import three_strike


class TestThreeStrike(unittest.TestCase):

    def test_three_strike1(self):
        result = three_strike.solution(45)
        self.assertEqual(result, 7)

    def test_three_strike2(self):
        result = three_strike.solution(125)
        self.assertEqual(result, 229)


if __name__ == '__main__':
    unittest.main()
