import unittest
import largest_number


class TestLargestNumber(unittest.TestCase):

    def test_largest_number1(self):
        result = largest_number.solution([6, 10, 2])
        self.assertEqual(result, "6210")

    def test_largest_number2(self):
        result = largest_number.solution([3, 30, 34, 5, 9])
        self.assertEqual(result, "9534330")

    def test_largest_number3(self):
        result = largest_number.solution([0, 0, 0, 0])
        self.assertEqual(result, "0")


if __name__ == '__main__':
    unittest.main()
