import unittest
import movingTraveler


class TestMovingTraveler(unittest.TestCase):

    def test_movingTraveler(self):
        result = movingTraveler.solution(5, 'R R R U D D')
        self.assertEqual(result, (3, 4))


if __name__ == '__main__':
    unittest.main()
