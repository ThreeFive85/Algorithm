import unittest
import string_compression


class TestStringCompression(unittest.TestCase):

    def test_string_compression1(self):
        result = string_compression.solution("aabbaccc")
        self.assertEqual(result, 7)

    def test_string_compression2(self):
        result = string_compression.solution("ababcdcdababcdcd")
        self.assertEqual(result, 9)

    def test_string_compression3(self):
        result = string_compression.solution("abcabcdede")
        self.assertEqual(result, 8)

    def test_string_compression4(self):
        result = string_compression.solution("abcabcabcabcdededededede")
        self.assertEqual(result, 14)

    def test_string_compression5(self):
        result = string_compression.solution("xababcdcdababcdcd")
        self.assertEqual(result, 17)


if __name__ == '__main__':
    unittest.main()
