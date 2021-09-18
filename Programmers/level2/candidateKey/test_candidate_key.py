import unittest
import candidate_key


class TestCandidateKey(unittest.TestCase):

    def test_candidate_key1(self):
        element = [["100", "ryan", "music", "2"],
                   ["200", "apeach", "math", "2"],
                   ["300", "tube", "computer", "3"],
                   ["400", "con", "computer", "4"],
                   ["500", "muzi", "music", "3"],
                   ["600", "apeach", "music", "2"]]
        result = candidate_key.solution(element)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
