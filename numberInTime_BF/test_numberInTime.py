import unittest
import numberInTime


class TestNumberInTime(unittest.TestCase):

    def test_numberInTime(self):
        result = numberInTime.solution(5)
        self.assertEqual(result, 11475)


if __name__ == '__main__':
    unittest.main()
