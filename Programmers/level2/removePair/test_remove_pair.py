import unittest
import remove_pair


class TestRemovePair(unittest.TestCase):

    def test_remove_pair1(self):
        argument = "baabaa"
        result = remove_pair.solution(argument)
        self.assertEqual(result, 1)

    def test_remove_pair2(self):
        argument = "abab"
        result = remove_pair.solution(argument)
        self.assertEqual(result, 0)

    def test_remove_pair3(self):
        argument = "aabbzz"
        result = remove_pair.solution(argument)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
