import unittest
import maxminLottos


class TestMaxminLottos(unittest.TestCase):

    def test_maxminLottos1(self):
        result = maxminLottos.solution(
            [44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])
        self.assertEqual(result, [3, 5])

    def test_maxminLottos2(self):
        result = maxminLottos.solution(
            [0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25])
        self.assertEqual(result, [1, 6])

    def test_maxminLottos3(self):
        result = maxminLottos.solution(
            [45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35])
        self.assertEqual(result, [1, 1])


if __name__ == '__main__':
    unittest.main()
