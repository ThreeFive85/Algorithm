import unittest
import make_prime


class TestMakePrime(unittest.TestCase):

    def test_make_prime1(self):
        argument = [1, 2, 3, 4]
        result = make_prime.solution(argument)
        self.assertEqual(result, 1)

    def test_make_prime2(self):
        argument = [1, 2, 7, 6, 4]
        result = make_prime.solution(argument)
        self.assertEqual(result, 4)

    def test_make_prime3(self):
        argument = [1, 2, 3]
        result = make_prime.solution(argument)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
