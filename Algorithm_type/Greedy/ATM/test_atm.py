import unittest
import atm


class TestAtm(unittest.TestCase):

    def atm1(self):
        result = atm.solution(5, [3, 1, 4, 3, 2])
        self.assertEqual(result, 32)

    def atm2(self):
        result = atm.solution(1, [5])
        self.assertEqual(result, 5)

    def atm3(self):
        result = atm.solution(3, [8, 1, 6])
        self.assertEqual(result, 23)


if __name__ == '__main__':
    unittest.main()
