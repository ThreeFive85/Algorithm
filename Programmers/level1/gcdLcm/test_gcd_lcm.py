import unittest
import gcd_lcm


class TestGcdLcm(unittest.TestCase):

    def test_gcd_lcm1(self):
        result = gcd_lcm.solution(3, 12)
        self.assertEqual(result, [3, 12])

    def test_gcd_lcm2(self):
        result = gcd_lcm.solution(2, 5)
        self.assertEqual(result, [1, 10])

    def test_gcd_lcm3(self):
        result = gcd_lcm.solution(1, 1)
        self.assertEqual(result, [1, 1])


if __name__ == '__main__':
    unittest.main()
