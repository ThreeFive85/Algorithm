import unittest
import triangle_snail


class TestTriangleSnail(unittest.TestCase):

    def test_triangle_snail1(self):
        result = triangle_snail.solution(4)
        self.assertEqual(result, [1, 2, 9, 3, 10, 8, 4, 5, 6, 7])

    def test_triangle_snail2(self):
        result = triangle_snail.solution(5)
        self.assertEqual(result, [1, 2, 12, 3, 13, 11,
                                  4, 14, 15, 10, 5, 6, 7, 8, 9])

    def test_triangle_snail3(self):
        result = triangle_snail.solution(6)
        self.assertEqual(result, [1, 2, 15, 3, 16, 14, 4,
                                  17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11])


if __name__ == '__main__':
    unittest.main()
