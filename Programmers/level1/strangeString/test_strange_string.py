import unittest
import strange_string


class TestStrangeString(unittest.TestCase):

    def test_strange_string1(self):
        result = strange_string.solution("try hello world")
        self.assertEqual(result, "TrY HeLlO WoRlD")

    def test_strange_string2(self):
        result = strange_string.solution("HELLO")
        self.assertEqual(result, "HeLlO")

    def test_strange_string3(self):
        result = strange_string.solution("good")
        self.assertEqual(result, "GoOd")


if __name__ == '__main__':
    unittest.main()
