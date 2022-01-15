import unittest
import rotateMatrix


class TestRotateMatrix(unittest.TestCase):

    def test_rotateMatrix1(self):
        argument1 = 6
        argument2 = 6
        argument3 = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
        result = rotateMatrix.solution(argument1, argument2, argument3)
        self.assertEqual(result, [8, 10, 25])

    def test_rotateMatrix2(self):
        argument1 = 3
        argument2 = 3
        argument3 = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
        result = rotateMatrix.solution(argument1, argument2, argument3)
        self.assertEqual(result, [1, 1, 5, 3])

    def test_rotateMatrix3(self):
        argument1 = 100
        argument2 = 97
        argument3 = [[1, 1, 100, 97]]
        result = rotateMatrix.solution(argument1, argument2, argument3)
        self.assertEqual(result, [1])


if __name__ == '__main__':
    unittest.main()
