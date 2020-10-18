import unittest
import descending_int


class TestStrangeString(unittest.TestCase):

    def test_descending_int1(self):
        result = descending_int.solution(123)
        self.assertEqual(result, 321)

    def test_descending_int2(self):
        result = descending_int.solution(12345)
        self.assertEqual(result, 54321)

    def test_descending_int3(self):
        result = descending_int.solution(116632)
        self.assertEqual(result, 663211)


if __name__ == '__main__':
    unittest.main()
