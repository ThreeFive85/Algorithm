import unittest
import tirdness


class TestTirdness(unittest.TestCase):

    def test_tirdness1(self):
        result = tirdness.solution(80, [[80, 20], [50, 40], [30, 10]])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
