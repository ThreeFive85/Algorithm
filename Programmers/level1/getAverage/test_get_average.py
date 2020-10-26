import unittest
import get_average


class TestGetAverage(unittest.TestCase):

    def test_get_average1(self):
        result = get_average.solution([1, 2, 3, 4])
        self.assertEqual(result, 2.5)

    def test_get_average2(self):
        result = get_average.solution([5, 5])
        self.assertEqual(result, 5)

    def test_get_average3(self):
        result = get_average.solution([0])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
