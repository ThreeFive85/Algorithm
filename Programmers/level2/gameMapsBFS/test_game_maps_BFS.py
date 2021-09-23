import unittest
import game_maps_BFS


class TestGameMapsBFS(unittest.TestCase):

    def test_game_maps_BFS1(self):
        element1 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
            1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
        result = game_maps_BFS.solution(element1)
        self.assertEqual(result, 11)

    def test_game_maps_BFS2(self):
        element1 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
            1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
        result = game_maps_BFS.solution(element1)
        self.assertEqual(result, -1)


if __name__ == '__main__':
    unittest.main()
