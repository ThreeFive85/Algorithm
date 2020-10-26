import unittest
import harshad_number


class TestHarshadNumber(unittest.TestCase):

    def test_harshad_number1(self):
        result = harshad_number.solution(10)
        self.assertEqual(result, True)

    def test_harshad_number2(self):
        result = harshad_number.solution(11)
        self.assertEqual(result, False)

    def test_harshad_number3(self):
        result = harshad_number.solution(12)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
