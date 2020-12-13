import unittest
import chain_english


class TestChainEnglish(unittest.TestCase):

    def test_chain_english1(self):
        argument1 = 3
        argument2 = ['tank', 'kick', 'know', 'wheel',
                     'land', 'dream', 'mother', 'robot', 'tank']
        result = chain_english.solution(argument1, argument2)
        self.assertEqual(result, [3, 3])

    def test_chain_english2(self):
        argument1 = 2
        argument2 = ['apple', 'element']
        result = chain_english.solution(argument1, argument2)
        self.assertEqual(result, [0, 0])

    def test_chain_english3(self):
        argument1 = 2
        argument2 = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
        result = chain_english.solution(argument1, argument2)
        self.assertEqual(result, [1, 3])


if __name__ == '__main__':
    unittest.main()
