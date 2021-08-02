# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/81301?language=python3

def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four',
             'five', 'six', 'seven', 'eight', 'nine']
    string = ''
    word = ''
    for i in range(len(s)):
        if s[i].isdigit():
            string += s[i]
        if s[i].isalpha():
            word += s[i]
            if word in words:
                string += str(words.index(word))
                word = ''
    # print(string)
    return int(string)
