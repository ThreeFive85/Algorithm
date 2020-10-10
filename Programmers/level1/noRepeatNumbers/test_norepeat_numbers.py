import unittest
import norepeat_numbers


class TestNoRepeatNumbers(unittest.TestCase):

    def test_norepeat_numbers1(self):
        result = norepeat_numbers.solution([1, 1, 3, 3, 0, 1, 1])
        self.assertEqual(result, [1, 3, 0, 1])

    def test_norepeat_numbers2(self):
        result = norepeat_numbers.solution([4, 4, 4, 5, 5])
        self.assertEqual(result, [4, 5])

    def test_norepeat_numbers3(self):
        result = norepeat_numbers.solution([1])
        self.assertEqual(result, [1])


if __name__ == '__main__':
    unittest.main()
