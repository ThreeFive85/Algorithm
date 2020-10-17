import unittest
import sum_digit


class TestStrangeString(unittest.TestCase):

    def test_sum_digit1(self):
        result = sum_digit.solution(123)
        self.assertEqual(result, 6)

    def test_sum_digit2(self):
        result = sum_digit.solution(12)
        self.assertEqual(result, 3)

    def test_sum_digit3(self):
        result = sum_digit.solution(0)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
