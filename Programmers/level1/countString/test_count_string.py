import unittest
import count_string


class TestCountString(unittest.TestCase):

    def test_count_string1(self):
        result = count_string.solution("pPoooyY")
        self.assertEqual(result, True)

    def test_count_string2(self):
        result = count_string.solution("Pyy")
        self.assertEqual(result, False)

    def test_count_string3(self):
        result = count_string.solution("ppyY")
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
