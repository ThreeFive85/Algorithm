import unittest
import save_boat


class TestSaveBoat(unittest.TestCase):

    def test_save_boat1(self):
        result = save_boat.solution([70, 50, 80, 50], 100)
        self.assertEqual(result, 3)

    def test_save_boat2(self):
        result = save_boat.solution([50, 70, 80], 100)
        self.assertEqual(result, 3)

    def test_save_boat3(self):
        result = save_boat.solution([100, 80, 60, 50], 100)
        self.assertEqual(result, 4)


if __name__ == '__main__':
    unittest.main()
