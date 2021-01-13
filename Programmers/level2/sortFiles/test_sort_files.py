import unittest
import sort_files


class TestSortFiles(unittest.TestCase):

    def test_sort_files1(self):
        argument = ["img12.png", "img10.png", "img02.png",
                    "img1.png", "IMG01.GIF", "img2.JPG"]
        result = sort_files.solution(argument)
        self.assertEqual(result, ["img1.png", "IMG01.GIF",
                                  "img02.png", "img2.JPG", "img10.png", "img12.png"])

    def test_sort_files2(self):
        argument = ["F-5 Freedom Fighter", "B-50 Superfortress",
                    "A-10 Thunderbolt II", "F-14 Tomcat"]
        result = sort_files.solution(argument)
        self.assertEqual(result, [
                         "A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"])


if __name__ == '__main__':
    unittest.main()
