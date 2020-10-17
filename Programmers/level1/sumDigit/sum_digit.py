# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0
    str_n = str(n)
    for int_n in str_n:
        answer += int(int_n)

    print(answer)
    return answer
