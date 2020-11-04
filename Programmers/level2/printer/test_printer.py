import unittest
import printer


class TestPrinter(unittest.TestCase):

    def test_printer1(self):
        result = printer.printer([2, 1, 3, 2], 2)
        self.assertEqual(result, 1)

    def test_printer2(self):
        result = printer.printer([1, 1, 9, 1, 1, 1], 0)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
