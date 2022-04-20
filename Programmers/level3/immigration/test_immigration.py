import unittest
import immigration


class TestImmigration(unittest.TestCase):

    def test_immigration1(self):
        element1 = 6
        element2 = [7, 10]
        result = immigration.solution(element1, element2)
        self.assertEqual(result, 28)


if __name__ == '__main__':
    unittest.main()
