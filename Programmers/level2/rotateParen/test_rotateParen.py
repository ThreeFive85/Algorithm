import unittest
import rotateParen


class TestRotateParen(unittest.TestCase):

    def test_save_boat1(self):
        result = rotateParen.solution("[](){}")
        self.assertEqual(result, 3)

    def test_save_boat2(self):
        result = rotateParen.solution("}]()[{")
        self.assertEqual(result, 2)

    def test_save_boat3(self):
        result = rotateParen.solution("[)(]")
        self.assertEqual(result, 0)

    def test_save_boat4(self):
        result = rotateParen.solution("}}}")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
