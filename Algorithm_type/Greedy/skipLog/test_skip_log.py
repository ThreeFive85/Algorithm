import unittest
import skip_log


class TestSkipLog(unittest.TestCase):

    def skip_log1(self):
        result = skip_log.solution(7, [13, 10, 12, 11, 10, 11, 12])
        self.assertEqual(result, 1)

    def skip_log2(self):
        result = skip_log.solution(5, [2, 4, 5, 7, 9])
        self.assertEqual(result, 4)

    def skip_log3(self):
        result = skip_log.solution(8, [6, 6, 6, 6, 6, 6, 6, 6])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
