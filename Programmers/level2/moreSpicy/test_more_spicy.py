import unittest
import more_spicy


class TestMoreSpicy(unittest.TestCase):

    def test_more_spicy1(self):
        result = more_spicy.solution([1, 2, 3, 9, 10, 12], 7)
        self.assertEqual(result, 2)

    def test_more_spicy2(self):
        result = more_spicy.solution([1, 1, 2, 6], 3)
        self.assertEqual(result, 2)

    def test_more_spicy3(self):
        result = more_spicy.solution([1, 1, 2, 6], 100)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
