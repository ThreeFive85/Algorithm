import unittest
import number_masking


class TestNumberMasking(unittest.TestCase):

    def test_number_masking1(self):
        result = number_masking.solution("01033334444")
        self.assertEqual(result, "*******4444")

    def test_number_masking2(self):
        result = number_masking.solution("027778888")
        self.assertEqual(result, "*****8888")

    def test_number_masking3(self):
        result = number_masking.solution("0511234567")
        self.assertEqual(result, "******4567")


if __name__ == '__main__':
    unittest.main()
