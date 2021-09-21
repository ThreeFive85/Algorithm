import unittest
import n_expressionDP


class TestNExpressionDP(unittest.TestCase):

    def test_n_expressionDP1(self):
        element1 = 5
        element2 = 12
        result = n_expressionDP.solution(element1, element2)
        self.assertEqual(result, 4)

    def test_n_expressionDP2(self):
        element1 = 2
        element2 = 11
        result = n_expressionDP.solution(element1, element2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
