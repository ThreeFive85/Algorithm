import unittest
import right_bracket


class TestRightBracket(unittest.TestCase):

    def test_right_bracket1(self):
        argument = "()()"
        result = right_bracket.solution(argument)
        self.assertEqual(result, True)

    def test_right_bracket2(self):
        argument = "(())()"
        result = right_bracket.solution(argument)
        self.assertEqual(result, True)

    def test_right_bracket3(self):
        argument = ")()("
        result = right_bracket.solution(argument)
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
