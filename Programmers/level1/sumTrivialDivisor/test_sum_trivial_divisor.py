import unittest
import sum_trivial_divisor


class TestSumTrivialDivisor(unittest.TestCase):

    def test_sum_trivial_divisor1(self):
        result = sum_trivial_divisor.solution(12)
        self.assertEqual(result, 28)

    def test_sum_trivial_divisor2(self):
        result = sum_trivial_divisor.solution(5)
        self.assertEqual(result, 6)

    def test_sum_trivial_divisor3(self):
        result = sum_trivial_divisor.solution(1)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
