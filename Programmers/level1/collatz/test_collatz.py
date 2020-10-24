import unittest
import collatz


class TestGcdLcm(unittest.TestCase):

    def test_collatz1(self):
        result = collatz.solution(6)
        self.assertEqual(result, 8)

    def test_collatz2(self):
        result = collatz.solution(16)
        self.assertEqual(result, 4)

    def test_collatz3(self):
        result = collatz.solution(626331)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
