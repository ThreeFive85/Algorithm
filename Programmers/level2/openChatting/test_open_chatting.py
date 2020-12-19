import unittest
import open_chatting


class TestOpenChatting(unittest.TestCase):

    def test_open_chatting1(self):
        argument1 = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
                     "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
        result = open_chatting.solution(argument1)
        self.assertEqual(result, [
                         "Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."])


if __name__ == '__main__':
    unittest.main()
