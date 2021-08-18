import unittest
import check_scores


class TestCheckScores(unittest.TestCase):

    def test_check_scores1(self):
        element = [[100, 90, 98, 88, 65], [50, 45, 99, 85, 77], [
            47, 88, 95, 80, 67], [61, 57, 100, 80, 65], [24, 90, 94, 75, 65]]
        result = check_scores.solution(element)
        self.assertEqual(result, "FBABD")

    def test_check_scores2(self):
        element = [[50, 90], [50, 87]]
        result = check_scores.solution(element)
        self.assertEqual(result, "DA")

    def test_check_scores3(self):
        element = [[70, 49, 90], [68, 50, 38], [73, 31, 100]]
        result = check_scores.solution(element)
        self.assertEqual(result, "CFD")

    def test_check_scores4(self):
        element = [[70, 70, 70, 70], [50, 50, 50, 50],
                   [70, 70, 70, 70], [50, 50, 50, 50]]
        result = check_scores.solution(element)
        self.assertEqual(result, "DDDD")


if __name__ == '__main__':
    unittest.main()
