import unittest
import secret_map


class TestSecretMap(unittest.TestCase):

    def test_secret_map1(self):
        n = 5
        arr1 = [9, 20, 28, 18, 11]
        arr2 = [30, 1, 21, 17, 28]
        result = secret_map.solution(n, arr1, arr2)
        self.assertEqual(result, ["#####", "# # #", "### #", "#  ##", "#####"])

    def test_secret_map2(self):
        n = 6
        arr1 = [46, 33, 33, 22, 31, 50]
        arr2 = [27, 56, 19, 14, 14, 10]
        result = secret_map.solution(n, arr1, arr2)
        self.assertEqual(result, ["######", "###  #",
                                  "##  ##", " #### ", " #####", "### # "])


if __name__ == '__main__':
    unittest.main()
