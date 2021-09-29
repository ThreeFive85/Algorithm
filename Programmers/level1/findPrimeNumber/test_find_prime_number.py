import unittest
import find_prime_number


class TestFindPrimeNumber(unittest.TestCase):

    def test_find_prime_number1(self):
        element1 = 10
        result = find_prime_number.solution(element1)
        self.assertEqual(result, 4)

    def test_find_prime_number2(self):
        element1 = 5
        result = find_prime_number.solution(element1)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
