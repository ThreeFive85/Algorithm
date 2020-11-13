import unittest
import make_big_number


class TestMakeBigNumber(unittest.TestCase):

    def test_make_big_number1(self):
        result = make_big_number.solution("1924", 2)
        self.assertEqual(result, "94")

    def test_make_big_number2(self):
        result = make_big_number.solution("1231234", 3)
        self.assertEqual(result, "3234")

    def test_make_big_number3(self):
        result = make_big_number.solution("4177252841", 4)
        self.assertEqual(result, "775841")


if __name__ == '__main__':
    unittest.main()
