import unittest
import expect_tournament


class TestExpectTournament(unittest.TestCase):

    def test_expect_tournament1(self):
        result = expect_tournament.solution(8, 4, 7)
        self.assertEqual(result, 3)

    def test_expect_tournament2(self):
        result = expect_tournament.solution(8, 4, 5)
        self.assertEqual(result, 3)

    def test_expect_tournament3(self):
        result = expect_tournament.solution(2, 1, 2)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
