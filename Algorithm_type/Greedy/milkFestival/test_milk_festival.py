import unittest
import milk_festival


class TestMilkFestival(unittest.TestCase):

    def milk_festival1(self):
        result = milk_festival.solution(7, [0, 1, 2, 0, 1, 2, 0])
        self.assertEqual(result, 7)

    def milk_festival2(self):
        result = milk_festival.solution(7, [2, 1, 1, 0, 0, 1, 2])
        self.assertEqual(result, 2)

    def milk_festival3(self):
        result = milk_festival.solution(3, [1, 2, 0])
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
