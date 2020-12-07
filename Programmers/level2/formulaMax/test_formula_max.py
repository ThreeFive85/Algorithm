import unittest
import formula_max


class TestFormulaMax(unittest.TestCase):

    def test_formula_max1(self):
        argument = "100-200*300-500+20"
        result = formula_max.solution(argument)
        self.assertEqual(result, 60420)

    def test_formula_max2(self):
        argument = "50*6-3*2"
        result = formula_max.solution(argument)
        self.assertEqual(result, 300)

    def test_formula_max3(self):
        argument = "1*1-101"
        result = formula_max.solution(argument)
        self.assertEqual(result, 100)


if __name__ == '__main__':
    unittest.main()
