import unittest
import far_node


class TestFarNode(unittest.TestCase):

    def test_far_node1(self):
        element1 = 6
        element2 = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
        result = far_node.solution(element1, element2)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
