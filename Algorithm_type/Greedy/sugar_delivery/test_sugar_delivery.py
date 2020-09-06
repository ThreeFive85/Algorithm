import unittest
import sugar_delivery


class TestSugarDelivery(unittest.TestCase):

    def test_sugar_delivery1(self):
        result = sugar_delivery.solution(18)
        self.assertEqual(result, 4)

    def test_sugar_delivery2(self):
        result = sugar_delivery.solution(4)
        self.assertEqual(result, -1)

    def test_sugar_delivery3(self):
        result = sugar_delivery.solution(6)
        self.assertEqual(result, 2)

    def test_sugar_delivery4(self):
        result = sugar_delivery.solution(9)
        self.assertEqual(result, 3)

    def test_sugar_delivery5(self):
        result = sugar_delivery.solution(11)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
