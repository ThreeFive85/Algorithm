import unittest
import express_number


class TestExpressNumber(unittest.TestCase):

    def test_express_number1(self):
        argument = 15
        result = express_number.solution(argument)
        self.assertEqual(result, 4)

    def test_express_number2(self):
        argument = 20
        result = express_number.solution(argument)
        self.assertEqual(result, 2)

    def test_express_number3(self):
        argument = 1
        result = express_number.solution(argument)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
