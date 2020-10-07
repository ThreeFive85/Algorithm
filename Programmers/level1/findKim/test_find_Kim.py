import unittest
import find_Kim


class TestFindKim(unittest.TestCase):

    def test_find_Kim1(self):
        result = find_Kim.solution(["Kim", "Park"])
        self.assertEqual(result, "김서방은 0에 있다")

    def test_find_Kim2(self):
        result = find_Kim.solution(["Lee", "Kim", "Park"])
        self.assertEqual(result, "김서방은 1에 있다")

    def test_find_Kim3(self):
        result = find_Kim.solution(["Song", "Lee", "Kim", "Park"])
        self.assertEqual(result, "김서방은 2에 있다")


if __name__ == '__main__':
    unittest.main()
