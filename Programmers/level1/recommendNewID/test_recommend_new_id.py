import unittest
import recommend_new_id


class TestRecommendNewID(unittest.TestCase):

    def test_recommend_new_id1(self):
        result = recommend_new_id.solution("...!@BaT#*..y.abcdefghijklm")
        self.assertEqual(result, "bat.y.abcdefghi")

    def test_recommend_new_id2(self):
        result = recommend_new_id.solution("z-+.^.")
        self.assertEqual(result, "z--")

    def test_recommend_new_id3(self):
        result = recommend_new_id.solution("=.=")
        self.assertEqual(result, "aaa")


if __name__ == '__main__':
    unittest.main()
