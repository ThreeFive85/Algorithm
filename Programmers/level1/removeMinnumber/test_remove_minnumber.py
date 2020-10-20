import unittest
import remove_minnumber


class TestRemoveMinNumber(unittest.TestCase):

    def test_remove_minnumber1(self):
        result = remove_minnumber.solution([4, 3, 2, 1])
        self.assertEqual(result, [4, 3, 2])

    def test_remove_minnumber2(self):
        result = remove_minnumber.solution([3])
        self.assertEqual(result, [-1])

    def test_remove_minnumber3(self):
        result = remove_minnumber.solution([1, 1, 1])
        self.assertEqual(result, [1, 1])


if __name__ == '__main__':
    unittest.main()
