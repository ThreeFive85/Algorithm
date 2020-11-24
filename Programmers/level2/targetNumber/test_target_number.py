import unittest
import target_number


class TestTargetNumber(unittest.TestCase):

    def test_target_number1(self):
        result = target_number.solution([1, 1, 1, 1, 1], 3)
        self.assertEqual(result, 5)

    def test_target_number2(self):
        result = target_number.solution([2, 1, 4, 1], 6)
        self.assertEqual(result, 2)

    def test_target_number3(self):
        result = target_number.solution([1, 1, 1, 1, 1], 2)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
