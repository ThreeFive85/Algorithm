import unittest
import cache_cities


class TestCacheCities(unittest.TestCase):

    def test_cache_cities1(self):
        argument1 = 3
        argument2 = ["Jeju", "Pangyo", "Seoul", "NewYork",
                     "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
        result = cache_cities.solution(argument1, argument2)
        self.assertEqual(result, 50)

    def test_cache_cities2(self):
        argument1 = 3
        argument2 = ["Jeju", "Pangyo", "Seoul", "Jeju",
                     "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
        result = cache_cities.solution(argument1, argument2)
        self.assertEqual(result, 21)

    def test_cache_cities3(self):
        argument1 = 0
        argument2 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
        result = cache_cities.solution(argument1, argument2)
        self.assertEqual(result, 25)


if __name__ == '__main__':
    unittest.main()
