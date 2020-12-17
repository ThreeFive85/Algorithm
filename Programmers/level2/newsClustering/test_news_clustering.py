import unittest
import news_clustering


class TestNewsClustering(unittest.TestCase):

    def test_news_clustering1(self):
        argument1 = "FRANCE"
        argument2 = "french"
        result = news_clustering.solution(argument1, argument2)
        self.assertEqual(result, 16384)

    def test_news_clustering2(self):
        argument1 = "handshake"
        argument2 = "shake hands"
        result = news_clustering.solution(argument1, argument2)
        self.assertEqual(result, 65536)

    def test_news_clustering3(self):
        argument1 = "E=M*C^2"
        argument2 = "e=m*c^2"
        result = news_clustering.solution(argument1, argument2)
        self.assertEqual(result, 65536)


if __name__ == '__main__':
    unittest.main()
