import unittest
import repeat_changebin


class TestRepeatChangeBin(unittest.TestCase):

    def test_repeat_changebin1(self):
        argument = "110010101001"
        result = repeat_changebin.solution(argument)
        self.assertEqual(result, [3, 8])

    def test_repeat_changebin2(self):
        argument = "01110"
        result = repeat_changebin.solution(argument)
        self.assertEqual(result, [3, 3])

    def test_repeat_changebin3(self):
        argument = "1111111"
        result = repeat_changebin.solution(argument)
        self.assertEqual(result, [4, 1])


if __name__ == '__main__':
    unittest.main()
