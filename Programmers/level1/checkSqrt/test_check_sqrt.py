import unittest
import check_sqrt


class TestCheckSqrt(unittest.TestCase):

    def test_check_sqrt1(self):
        result = check_sqrt.solution(121)
        self.assertEqual(result, 144)

    def test_check_sqrt2(self):
        result = check_sqrt.solution(3)
        self.assertEqual(result, -1)

    def test_check_sqrt3(self):
        result = check_sqrt.solution(4)
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
