# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    list_n = sorted(str(n), reverse=True)
    result = "".join(list_n)

    print(int(result))
    return int(result)
