import unittest
import stringNumberAndAlpha


class TestStringNumberAndAlpha(unittest.TestCase):

    def test_stringNumberAndAlpha1(self):
        result = stringNumberAndAlpha.solution("one4seveneight")
        self.assertEqual(result, 1478)

    def test_stringNumberAndAlpha2(self):
        result = stringNumberAndAlpha.solution("23four5six7")
        self.assertEqual(result, 234567)

    def test_stringNumberAndAlpha3(self):
        result = stringNumberAndAlpha.solution("2three45sixseven")
        self.assertEqual(result, 234567)

    def test_stringNumberAndAlpha4(self):
        result = stringNumberAndAlpha.solution("123")
        self.assertEqual(result, 123)


if __name__ == '__main__':
    unittest.main()
