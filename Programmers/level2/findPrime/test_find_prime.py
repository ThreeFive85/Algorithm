import unittest
import find_prime


class TestFindPrime(unittest.TestCase):

    def test_find_prime1(self):
        result = find_prime.solution("17")
        self.assertEqual(result, 3)

    def test_find_prime2(self):
        result = find_prime.solution("011")
        self.assertEqual(result, 2)

    def test_find_prime3(self):
        result = find_prime.solution("1")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
