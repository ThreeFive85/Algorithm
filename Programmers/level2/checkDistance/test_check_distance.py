import unittest
import check_distance


class TestCheckDistance(unittest.TestCase):

    def test_check_distance1(self):
        element1 = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
                    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
        result = check_distance.solution(element1)
        self.assertEqual(result, [1, 0, 1, 1, 1])


if __name__ == '__main__':
    unittest.main()
