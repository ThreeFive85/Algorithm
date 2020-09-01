import unittest
import untilOne


class TestUntilone(unittest.TestCase):

    def test_untilOne1(self):
        result = untilOne.solution(32, 7)
        self.assertEqual(result, 8)

    def test_untilOne2(self):
        result = untilOne.solution(17, 4)
        self.assertEqual(result, 3)

    def test_untilOne3(self):
        result = untilOne.solution(25, 3)
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
