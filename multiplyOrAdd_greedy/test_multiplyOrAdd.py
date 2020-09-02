import unittest
import multiplyOrAdd


class TestMultiplyOrAdd(unittest.TestCase):

    def test_multiplyOrAdd1(self):
        result = multiplyOrAdd.solution("02984")
        self.assertEqual(result, 576)

    def test_multiplyOrAdd2(self):
        result = multiplyOrAdd.solution("576")
        self.assertEqual(result, 210)

    def test_multiplyOrAdd3(self):
        result = multiplyOrAdd.solution("123")
        self.assertEqual(result, 9)


if __name__ == '__main__':
    unittest.main()
