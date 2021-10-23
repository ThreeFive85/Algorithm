import unittest
import escape_maze


class TestEscapeMaze(unittest.TestCase):

    def test_escape_maze1(self):
        element1 = [[1, 0, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [
            0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
        result = escape_maze.solution(element1)
        self.assertEqual(result, 10)

    def test_escape_maze2(self):
        element1 = [[1, 1, 1], [1, 0, 1], [0, 0, 1]]
        result = escape_maze.solution(element1)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
