import unittest
import joystick


class TestJoystick(unittest.TestCase):

    def test_joystick1(self):
        result = joystick.solution("JEROEN")
        self.assertEqual(result, 56)

    def test_joystick2(self):
        result = joystick.solution("JAN")
        self.assertEqual(result, 23)


if __name__ == '__main__':
    unittest.main()
