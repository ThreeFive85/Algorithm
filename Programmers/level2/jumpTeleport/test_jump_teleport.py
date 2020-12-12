import unittest
import jump_teleport


class TestJumpTeleport(unittest.TestCase):

    def test_jump_teleport1(self):
        argument = 5
        result = jump_teleport.solution(argument)
        self.assertEqual(result, 2)

    def test_jump_teleport2(self):
        argument = 6
        result = jump_teleport.solution(argument)
        self.assertEqual(result, 2)

    def test_jump_teleport3(self):
        argument = 5000
        result = jump_teleport.solution(argument)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
