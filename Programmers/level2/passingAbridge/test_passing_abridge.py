import unittest
import passing_abridge


class TestPassingAbridge(unittest.TestCase):

    def test_passing_abridge1(self):
        result = passing_abridge.solution(2, 10, [7, 4, 5, 6])
        self.assertEqual(result, 8)

    def test_passing_abridge2(self):
        result = passing_abridge.solution(
            100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        self.assertEqual(result, 110)

    def test_passing_abridge3(self):
        result = passing_abridge.solution(100, 100, [10])
        self.assertEqual(result, 101)


if __name__ == '__main__':
    unittest.main()
