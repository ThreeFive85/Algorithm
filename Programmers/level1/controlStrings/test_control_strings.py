import unittest
import control_strings


class TestControlStrings(unittest.TestCase):

    def test_control_strings1(self):
        result = control_strings.solution("a234")
        self.assertEqual(result, False)

    def test_control_strings2(self):
        result = control_strings.solution("1234")
        self.assertEqual(result, True)

    def test_control_strings3(self):
        result = control_strings.solution("1")
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
