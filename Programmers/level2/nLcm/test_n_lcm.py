import unittest
import n_lcm


class TestNLcm(unittest.TestCase):

    def test_n_lcm1(self):
        argument = [2, 6, 8, 14]
        result = n_lcm.solution(argument)
        self.assertEqual(result, 168)

    def test_n_lcm2(self):
        argument = [1, 2, 3]
        result = n_lcm.solution(argument)
        self.assertEqual(result, 6)

    def test_n_lcm3(self):
        argument = [1, 2]
        result = n_lcm.solution(argument)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
