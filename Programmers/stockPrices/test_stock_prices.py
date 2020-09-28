import unittest
import stock_prices


class TestStockPrices(unittest.TestCase):

    def stock_prices1(self):
        result = stock_prices.solution([1, 2, 3, 2, 3])
        self.assertEqual(result, [4, 3, 1, 1, 0])


if __name__ == '__main__':
    unittest.main()
