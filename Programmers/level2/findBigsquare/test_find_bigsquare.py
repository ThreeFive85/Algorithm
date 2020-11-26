import unittest
import find_bigsquare


class TestFindBigSquare(unittest.TestCase):

    def test_find_bigsquare1(self):
        arr = [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]
        result = find_bigsquare.solution(arr)
        self.assertEqual(result, 9)

    def test_find_bigsquare2(self):
        arr = [[0, 0, 1, 1], [1, 1, 1, 1]]
        result = find_bigsquare.solution(arr)
        self.assertEqual(result, 4)

    def test_find_bigsquare3(self):
        arr = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        result = find_bigsquare.solution(arr)
        self.assertEqual(result, 16)


if __name__ == '__main__':
    unittest.main()
