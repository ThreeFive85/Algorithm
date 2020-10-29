import unittest
import failure_rate


class TestFailureRate(unittest.TestCase):

    def test_failure_rate1(self):
        n = 5
        stages = [2, 1, 2, 6, 2, 4, 3, 3]
        result = failure_rate.solution(n, stages)
        self.assertEqual(result, [3, 4, 2, 1, 5])

    def test_failure_rate2(self):
        n = 4
        stages = [4, 4, 4, 4, 4]
        result = failure_rate.solution(n, stages)
        self.assertEqual(result, [4, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()
