import unittest
import job_recommend


class TestJobRecommend(unittest.TestCase):

    def test_job_recommend1(self):
        element1 = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
                    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                    "GAME C++ C# JAVASCRIPT C JAVA"]
        element2 = ["PYTHON", "C++", "SQL"]
        element3 = [7, 5, 5]
        result = job_recommend.solution(element1, element2, element3)
        self.assertEqual(result, "HARDWARE")

    def test_job_recommend2(self):
        element1 = ["SI JAVA JAVASCRIPT SQL PYTHON C#",
                    "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
                    "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
                    "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
                    "GAME C++ C# JAVASCRIPT C JAVA"]
        element2 = ["JAVA", "JAVASCRIPT"]
        element3 = [7, 5]
        result = job_recommend.solution(element1, element2, element3)
        self.assertEqual(result, "PORTAL")


if __name__ == '__main__':
    unittest.main()
