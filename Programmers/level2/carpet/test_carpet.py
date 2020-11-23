import unittest
import carpet


class TestCarpet(unittest.TestCase):

    def test_carpet1(self):
        result = carpet.solution(10, 2)
        self.assertEqual(result, [4, 3])

    def test_carpet2(self):
        result = carpet.solution(8, 1)
        self.assertEqual(result, [3, 3])

    def test_carpet3(self):
        result = carpet.solution(24, 24)
        self.assertEqual(result, [8, 6])


if __name__ == '__main__':
    unittest.main()
