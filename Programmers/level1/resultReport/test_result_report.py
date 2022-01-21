import unittest
import result_report


class TestResultReport(unittest.TestCase):

    def test_result_report1(self):
        a = ["muzi", "frodo", "apeach", "neo"]
        b = ["muzi frodo", "apeach frodo",
             "frodo neo", "muzi neo", "apeach muzi"]
        c = 2
        result = result_report.solution(a, b, c)
        self.assertEqual(result, [2, 1, 1, 0])

    def test_result_report2(self):
        a = ["con", "ryan"]
        b = ["ryan con", "ryan con", "ryan con", "ryan con"]
        c = 3
        result = result_report.solution(a, b, c)
        self.assertEqual(result, [0, 0])


if __name__ == '__main__':
    unittest.main()
