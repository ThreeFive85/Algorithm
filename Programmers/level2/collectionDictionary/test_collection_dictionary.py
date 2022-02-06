import unittest
import collection_dictionary


class TestCollectionDictionary(unittest.TestCase):

    def test_collection_dictionary1(self):
        element1 = "AAAAE"
        result = collection_dictionary.solution(element1)
        self.assertEqual(result, 6)

    def test_collection_dictionary2(self):
        element1 = "AAAE"
        result = collection_dictionary.solution(element1)
        self.assertEqual(result, 10)

    def test_collection_dictionary3(self):
        element1 = "I"
        result = collection_dictionary.solution(element1)
        self.assertEqual(result, 1563)


if __name__ == '__main__':
    unittest.main()
