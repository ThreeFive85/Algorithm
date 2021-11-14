import unittest
import delivery


class TestDelivery(unittest.TestCase):

    def test_delivery1(self):
        result = delivery.solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [
                                   1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
        self.assertEqual(result, 4)

    def test_delivery2(self):
        result = delivery.solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
                                   3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
