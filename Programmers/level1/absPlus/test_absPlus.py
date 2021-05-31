import unittest
import absPlus


class TestAbsPlus(unittest.TestCase):

    def test_absPlus1(self):
        result = absPlus.solution([4, 7, 12], [True, False, True])
        self.assertEqual(result, 9)

    def test_absPlus2(self):
        result = absPlus.solution([1, 2, 3], [False, False, True])
        self.assertEqual(result, 0)

    def test_absPlus3(self):
        result = absPlus.solution([1, 2, 3], [True, True, True])
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()
