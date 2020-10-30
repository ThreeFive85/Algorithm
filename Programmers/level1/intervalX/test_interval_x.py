import unittest
import interval_x


class TestIntervalX(unittest.TestCase):

    def test_interval_x1(self):
        result = interval_x.solution(2, 5)
        self.assertEqual(result, [2, 4, 6, 8, 10])

    def test_interval_x2(self):
        result = interval_x.solution(4, 3)
        self.assertEqual(result, [4, 8, 12])

    def test_interval_x3(self):
        result = interval_x.solution(-4, 2)
        self.assertEqual(result, [-4, -8])


if __name__ == '__main__':
    unittest.main()
