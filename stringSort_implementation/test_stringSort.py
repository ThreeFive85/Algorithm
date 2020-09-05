import unittest
import stringSort


class TestStringSort(unittest.TestCase):

    def test_stringSort1(self):
        result = stringSort.solution("K1KA5CB7")
        self.assertEqual(result, "ABCKK13")

    def test_stringSort2(self):
        result = stringSort.solution("AJKDLSI412K4JSJ9D")
        self.assertEqual(result, "ADDIJJJKKLSS20")


if __name__ == '__main__':
    unittest.main()
