import unittest
import two_plus


class TestTwoPlus(unittest.TestCase):

    def test_two_plus1(self):
        result = two_plus.solution([2, 1, 3, 4, 1])
        self.assertEqual(result, [2, 3, 4, 5, 6, 7])

    def test_two_plus2(self):
        result = two_plus.solution([5, 0, 2, 7])
        self.assertEqual(result, [2, 5, 7, 9, 12])


if __name__ == '__main__':
    unittest.main()
