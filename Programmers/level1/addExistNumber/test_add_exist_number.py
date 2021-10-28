import unittest
import add_exist_number


class TestAddExistNumber(unittest.TestCase):

    def test_add_exist_number1(self):
        result = add_exist_number.solution([1, 2, 3, 4, 6, 7, 8, 0])
        self.assertEqual(result, 14)

    def test_add_exist_number2(self):
        result = add_exist_number.solution([5, 8, 4, 0, 6, 7, 9])
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
