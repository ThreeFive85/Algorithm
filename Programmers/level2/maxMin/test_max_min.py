import unittest
import max_min


class TestMaxMin(unittest.TestCase):

    def test_max_min1(self):
        argument = "1 2 3 4"
        result = max_min.solution(argument)
        self.assertEqual(result, "1 4")

    def test_max_min2(self):
        argument = "-1 -2 -3 -4"
        result = max_min.solution(argument)
        self.assertEqual(result, "-4 -1")

    def test_max_min3(self):
        argument = "-1 -1"
        result = max_min.solution(argument)
        self.assertEqual(result, "-1 -1")


if __name__ == '__main__':
    unittest.main()
