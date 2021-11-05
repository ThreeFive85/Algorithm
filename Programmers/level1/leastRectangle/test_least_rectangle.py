import unittest
import least_rectangle


class TestLeastRectangle(unittest.TestCase):

    def test_least_rectangle1(self):
        result = least_rectangle.solution(
            [[60, 50], [30, 70], [60, 30], [80, 40]])
        self.assertEqual(result, 4000)

    def test_least_rectangle2(self):
        result = least_rectangle.solution(
            [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
        self.assertEqual(result, 120)

    def test_least_rectangle3(self):
        result = least_rectangle.solution(
            [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])
        self.assertEqual(result, 133)


if __name__ == '__main__':
    unittest.main()
