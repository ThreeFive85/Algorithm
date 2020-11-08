import unittest
import functional_development


class TestFunctionalDevelopment(unittest.TestCase):

    def test_functional_development1(self):
        result = functional_development.solution([93, 30, 55], [1, 30, 5])
        self.assertEqual(result, [2, 1])

    def test_functional_development2(self):
        result = functional_development.solution(
            [95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
        self.assertEqual(result, [1, 3, 2])


if __name__ == '__main__':
    unittest.main()
