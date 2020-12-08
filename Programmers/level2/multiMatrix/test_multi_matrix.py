import unittest
import multi_matrix


class TestMultiMatrix(unittest.TestCase):

    def test_multi_matrix1(self):
        argument1 = [[1, 4], [3, 2], [4, 1]]
        argument2 = [[3, 3], [3, 3]]
        result = multi_matrix.solution(argument1, argument2)
        self.assertEqual(result, [[15, 15], [15, 15], [15, 15]])

    def test_multi_matrix2(self):
        argument1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
        argument2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
        result = multi_matrix.solution(argument1, argument2)
        self.assertEqual(result, [[22, 22, 11], [36, 28, 18], [29, 20, 14]])

    def test_multi_matrix3(self):
        argument1 = [[1]]
        argument2 = [[1]]
        result = multi_matrix.solution(argument1, argument2)
        self.assertEqual(result, [[1]])


if __name__ == '__main__':
    unittest.main()
