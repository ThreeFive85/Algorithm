import unittest
import odd_even


class TestOddEven(unittest.TestCase):

    def test_odd_even1(self):
        result = odd_even.solution(1)
        self.assertEqual(result, "Odd")

    def test_odd_even2(self):
        result = odd_even.solution(2)
        self.assertEqual(result, "Even")

    def test_odd_even3(self):
        result = odd_even.solution(0)
        self.assertEqual(result, "Even")


if __name__ == '__main__':
    unittest.main()
