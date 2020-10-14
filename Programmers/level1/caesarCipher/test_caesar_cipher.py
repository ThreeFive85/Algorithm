import unittest
import caesar_cipher


class TestCaesarCipher(unittest.TestCase):

    def test_caesar_cipher1(self):
        result = caesar_cipher.solution("AB", 1)
        self.assertEqual(result, "BC")

    def test_caesar_cipher2(self):
        result = caesar_cipher.solution("z", 1)
        self.assertEqual(result, "a")

    def test_caesar_cipher3(self):
        result = caesar_cipher.solution("a B z", 4)
        self.assertEqual(result, "e F d")


if __name__ == '__main__':
    unittest.main()
