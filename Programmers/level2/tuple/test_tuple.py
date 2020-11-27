import unittest
import tuple


class TestTuple(unittest.TestCase):

    def test_tuple1(self):
        arr = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
        result = tuple.solution(arr)
        self.assertEqual(result, [2, 1, 3, 4])

    def test_tuple2(self):
        arr = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
        result = tuple.solution(arr)
        self.assertEqual(result, [2, 1, 3, 4])

    def test_tuple3(self):
        arr = "{{20,111},{111}}"
        result = tuple.solution(arr)
        self.assertEqual(result, [111, 20])


if __name__ == '__main__':
    unittest.main()
