import unittest
import skill_tree


class TestSkillTree(unittest.TestCase):

    def test_skill_tree1(self):
        result = skill_tree.solution('CBD', ['BACDE', 'CBADF', 'AECB', 'BDA'])
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
