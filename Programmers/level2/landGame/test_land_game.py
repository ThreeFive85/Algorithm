import unittest
import land_game


class TestLandGame(unittest.TestCase):

    def test_land_game1(self):
        argument = [[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]
        result = land_game.solution(argument)
        self.assertEqual(result, 16)

    def test_land_game2(self):
        argument = [[5, 2, 1, 4], [6, 5, 4, 1], [7, 8, 1, 4], [1, 8, 6, 2]]
        result = land_game.solution(argument)
        self.assertEqual(result, 25)

    def test_land_game3(self):
        argument = [[5, 2, 1, 4], [100, 5, 4, 1], [7, 8, 1, 4], [1, 8, 6, 2]]
        result = land_game.solution(argument)
        self.assertEqual(result, 118)


if __name__ == '__main__':
    unittest.main()
