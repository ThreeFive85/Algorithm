import unittest
import change_bracket


class TestChangeBracket(unittest.TestCase):

    def test_change_bracket1(self):
        result = change_bracket.solution("(()())()")
        self.assertEqual(result, "(()())()")

    def test_change_bracket2(self):
        result = change_bracket.solution(")(")
        self.assertEqual(result, "()")

    def test_change_bracket3(self):
        result = change_bracket.solution("()))((()")
        self.assertEqual(result, "()(())()")


if __name__ == '__main__':
    unittest.main()
