import unittest
import to_integer


class TestThreeStrike(unittest.TestCase):

    def test_to_integer1(self):
        result = to_integer.solution("45")
        self.assertEqual(result, 45)

    def test_to_integer2(self):
        result = to_integer.solution("125")
        self.assertEqual(result, 125)

    def test_to_integer3(self):
        result = to_integer.solution("-125")
        self.assertEqual(result, -125)


if __name__ == '__main__':
    unittest.main()
