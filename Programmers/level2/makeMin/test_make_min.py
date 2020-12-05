import unittest
import make_min


class TestMakeMin(unittest.TestCase):

    def test_make_min1(self):
        argument1 = [1, 4, 2]
        argument2 = [5, 4, 4]
        result = make_min.solution(argument1, argument2)
        self.assertEqual(result, 29)

    def test_make_min2(self):
        argument1 = [1, 2]
        argument2 = [3, 4]
        result = make_min.solution(argument1, argument2)
        self.assertEqual(result, 10)

    def test_make_min3(self):
        argument1 = [1]
        argument2 = [3]
        result = make_min.solution(argument1, argument2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
