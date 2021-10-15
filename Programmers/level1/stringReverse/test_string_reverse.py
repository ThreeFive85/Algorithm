import unittest
import string_reverse


class TestStringReverse(unittest.TestCase):

    def test_sum_digit1(self):
        result = string_reverse.solution("Zbcdefg")
        self.assertEqual(result, "gfedcbZ")

    def test_sum_digit2(self):
        result = string_reverse.solution("abcx")
        self.assertEqual(result, "xcba")

    def test_sum_digit3(self):
        result = string_reverse.solution("aaa")
        self.assertEqual(result, "aaa")


if __name__ == '__main__':
    unittest.main()
