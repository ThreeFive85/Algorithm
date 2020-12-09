import unittest
import jaden_case


class TestJadenCase(unittest.TestCase):

    def test_jaden_case1(self):
        argument = "3people unFollowed me"
        result = jaden_case.solution(argument)
        self.assertEqual(result, "3people Unfollowed Me")

    def test_jaden_case2(self):
        argument = "for the last week"
        result = jaden_case.solution(argument)
        self.assertEqual(result, "For The Last Week")

    def test_jaden_case3(self):
        argument = " for  the last    week"
        result = jaden_case.solution(argument)
        self.assertEqual(result, " For  The Last    Week")


if __name__ == '__main__':
    unittest.main()
