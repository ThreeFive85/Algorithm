import unittest
import camouflage


class TestCamouflage(unittest.TestCase):

    def test_camouflage1(self):
        arg = [["yellow_hat", "headgear"], [
            "blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
        result = camouflage.solution(arg)
        self.assertEqual(result, 5)

    def test_camouflage2(self):
        arg = [["crow_mask", "face"], [
            "blue_sunglasses", "face"], ["smoky_makeup", "face"]]
        result = camouflage.solution(arg)
        self.assertEqual(result, 3)

    def test_camouflage3(self):
        arg = [["blue_sunglasses", "eyewear"]]
        result = camouflage.solution(arg)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
