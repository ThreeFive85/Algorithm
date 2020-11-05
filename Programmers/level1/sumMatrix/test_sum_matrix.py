import unittest
import sum_matrix


class TestSumMatrix(unittest.TestCase):

    def test_sum_matrix1(self):
        result = sum_matrix.solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])
        self.assertEqual(result, [[4, 6], [7, 9]])

    def test_sum_matrix2(self):
        result = sum_matrix.solution([[1], [2]], [[3], [4]])
        self.assertEqual(result, [[4], [6]])

    def test_sum_matrix3(self):
        result = sum_matrix.solution([[0]], [[1]])
        self.assertEqual(result, [[1]])


if __name__ == '__main__':
    unittest.main()
