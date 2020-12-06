import unittest
import fibonacci_number


class TestFibonacciNumber(unittest.TestCase):

    def test_fibonacci_number1(self):
        argument = 3
        result = fibonacci_number.solution(argument)
        self.assertEqual(result, 2)

    def test_fibonacci_number2(self):
        argument = 5
        result = fibonacci_number.solution(argument)
        self.assertEqual(result, 5)

    def test_fibonacci_number3(self):
        argument = 6
        result = fibonacci_number.solution(argument)
        self.assertEqual(result, 8)


if __name__ == '__main__':
    unittest.main()
