# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12926

import string


def solution(s, n):
    answer = ''
    for alpa in s:
        if alpa.isupper():
            idx = int(string.ascii_uppercase.index(alpa)) + n
            if idx > 25:
                idx = idx % 26
            answer += string.ascii_uppercase[idx]
        elif alpa.islower():
            idx = int(string.ascii_lowercase.index(alpa)) + n
            if idx > 25:
                idx = idx % 26
            answer += string.ascii_lowercase[idx]
        elif alpa == " ":
            answer += " "
    print(answer)
    return answer


# print(string.ascii_lowercase.index("z"))
solution("AB", 1)
solution("z", 1)
solution("a B z", 4)
