import unittest
import years_2016


class TestYears2016(unittest.TestCase):

    def test_2016years1(self):
        element1 = 5
        element2 = 24
        result = years_2016.solution(element1, element2)
        self.assertEqual(result, "TUE")


if __name__ == '__main__':
    unittest.main()
