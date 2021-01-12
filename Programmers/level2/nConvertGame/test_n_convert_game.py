import unittest
import n_convert_game


class TestNConvertGame(unittest.TestCase):

    def test_n_convert_game1(self):
        result = n_convert_game.solution(2, 4, 2, 1)
        self.assertEqual(result, "0111")

    def test_n_convert_game2(self):
        argument = 6
        result = n_convert_game.solution(16, 16, 2, 1)
        self.assertEqual(result, "02468ACE11111111")

    def test_n_convert_game3(self):
        argument = 5000
        result = n_convert_game.solution(16, 16, 2, 2)
        self.assertEqual(result, "13579BDF01234567")


if __name__ == '__main__':
    unittest.main()
