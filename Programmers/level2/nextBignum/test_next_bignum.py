import unittest
import next_bignum


class TestNextBigNum(unittest.TestCase):

    def test_next_bignum1(self):
        argument = 78
        result = next_bignum.solution(argument)
        self.assertEqual(result, 83)

    def test_next_bignum2(self):
        argument = 15
        result = next_bignum.solution(argument)
        self.assertEqual(result, 23)

    def test_next_bignum3(self):
        argument = 10
        result = next_bignum.solution(argument)
        self.assertEqual(result, 12)


if __name__ == '__main__':
    unittest.main()
