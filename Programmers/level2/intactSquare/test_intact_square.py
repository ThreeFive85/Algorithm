import unittest
import intact_square


class TestIntactSquare(unittest.TestCase):

    def test_intact_square1(self):
        result = intact_square.solution(8, 12)
        self.assertEqual(result, 80)


if __name__ == '__main__':
    unittest.main()
