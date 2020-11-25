import unittest
import quad_tree


class TestQuadTree(unittest.TestCase):

    def test_quad_tree1(self):
        arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
        result = quad_tree.solution(arr)
        self.assertEqual(result, [4, 9])

    def test_quad_tree2(self):
        arr = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
        result = quad_tree.solution(arr)
        self.assertEqual(result, [0, 1])

    def test_quad_tree3(self):
        arr = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        result = quad_tree.solution(arr)
        self.assertEqual(result, [1, 0])


if __name__ == '__main__':
    unittest.main()
