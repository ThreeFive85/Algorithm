import unittest
import divisorCntAndAdd


class TestDivisorCntAndAdd(unittest.TestCase):

    def test_divisorCntAndAdd1(self):
        result = divisorCntAndAdd.solution(13, 17)
        self.assertEqual(result, 43)

    def test_divisorCntAndAdd2(self):
        result = divisorCntAndAdd.solution(24, 27)
        self.assertEqual(result, 52)

    def test_divisorCntAndAdd3(self):
        result = divisorCntAndAdd.solution(1, 2)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
