import unittest
import budget


class TestBudget(unittest.TestCase):

    def test_budget1(self):
        result = budget.solution([1, 3, 2, 5, 4], 9)
        self.assertEqual(result, 3)

    def test_budget2(self):
        result = budget.solution([2, 2, 3, 3], 10)
        self.assertEqual(result, 4)

    def test_budget3(self):
        result = budget.solution([1], 1)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
