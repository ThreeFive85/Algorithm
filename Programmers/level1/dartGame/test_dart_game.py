import unittest
import dart_game


class TestDartGame(unittest.TestCase):

    def test_dart_game1(self):
        result = dart_game.solution("1S2D*3T")
        self.assertEqual(result, 37)

    def test_dart_game2(self):
        result = dart_game.solution("1T2D3D#")
        self.assertEqual(result, -4)

    def test_dart_game3(self):
        result = dart_game.solution("1D2S3T*")
        self.assertEqual(result, 59)


if __name__ == '__main__':
    unittest.main()
