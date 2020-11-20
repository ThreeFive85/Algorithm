import unittest
import phone_list


class TestPhoneList(unittest.TestCase):

    def test_phone_list1(self):
        result = phone_list.solution(["119", "97674223", "1195524421"])
        self.assertEqual(result, False)

    def test_phone_list2(self):
        result = phone_list.solution(["123", "456", "789"])
        self.assertEqual(result, True)

    def test_phone_list3(self):
        result = phone_list.solution(["12", "123", "1235", "567", "88"])
        self.assertEqual(result, False)


if __name__ == '__main__':
    unittest.main()
