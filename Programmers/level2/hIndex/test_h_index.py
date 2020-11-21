import unittest
import h_index


class TestHIndex(unittest.TestCase):

    def test_h_index1(self):
        result = h_index.solution([3, 0, 6, 1, 5])
        self.assertEqual(result, 3)

    def test_h_index2(self):
        result = h_index.solution([10, 50, 100])
        self.assertEqual(result, 3)

    def test_h_index3(self):
        result = h_index.solution([0, 1, 0, 0, 0, 0])
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
