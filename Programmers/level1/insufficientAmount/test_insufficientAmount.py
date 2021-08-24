import unittest
import insufficientAmount


class TestinsufficientAmount(unittest.TestCase):

    def test_insufficientAmount1(self):
        result = insufficientAmount.solution(3, 20, 4)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
