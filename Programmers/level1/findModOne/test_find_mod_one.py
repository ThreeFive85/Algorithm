import unittest
import find_mod_one


class TestFindModOne(unittest.TestCase):

    def test_find_mod_one1(self):
        result = find_mod_one.solution(10)
        self.assertEqual(result, 3)

    def test_find_mod_one2(self):
        result = find_mod_one.solution(12)
        self.assertEqual(result, 11)

    def test_find_mod_one3(self):
        result = find_mod_one.solution(3)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
