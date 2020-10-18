import unittest
import makelist_reverseint


class TestStrangeString(unittest.TestCase):

    def test_makelist_reverseint1(self):
        result = makelist_reverseint.solution(123)
        self.assertEqual(result, [3, 2, 1])

    def test_makelist_reverseint2(self):
        result = makelist_reverseint.solution(12345)
        self.assertEqual(result, [5, 4, 3, 2, 1])

    def test_makelist_reverseint3(self):
        result = makelist_reverseint.solution(0)
        self.assertEqual(result, [0])


if __name__ == '__main__':
    unittest.main()
