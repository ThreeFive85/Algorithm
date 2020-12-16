import unittest
import friends_block


class TestFriendBlock(unittest.TestCase):

    def test_friends_block1(self):
        argument1 = 4
        argument2 = 5
        argument3 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
        result = friends_block.solution(argument1, argument2, argument3)
        self.assertEqual(result, 14)

    def test_friends_block2(self):
        argument1 = 6
        argument2 = 6
        argument3 = ["TTTANT", "RRFACC", "RRRFCC",
                     "TRRRAA", "TTMMMF", "TMMTTJ"]
        result = friends_block.solution(argument1, argument2, argument3)
        self.assertEqual(result, 15)

    def test_friends_block3(self):
        argument1 = 6
        argument2 = 6
        argument3 = ["AABBEE", "AAAEEE", "VAAEEV",
                     "AABBEE", "AACCEE", "VVCCEE"]
        result = friends_block.solution(argument1, argument2, argument3)
        self.assertEqual(result, 32)


if __name__ == '__main__':
    unittest.main()
