import unittest
import iwant_sort_string


class TestIwantSortString(unittest.TestCase):

    def test_iwant_sort_string1(self):
        result = iwant_sort_string.solution(["sun", "bed", "car"], 1)
        self.assertEqual(result, ["car", "bed", "sun"])

    def test_iwant_sort_string2(self):
        result = iwant_sort_string.solution(["abce", "abcd", "cdx"], 2)
        self.assertEqual(result, ["abcd", "abce", "cdx"])


if __name__ == '__main__':
    unittest.main()
