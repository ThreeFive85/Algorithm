# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3

def solution(n):
    answer = ''
    while n > 0:
        if n % 3 == 0:
            answer = '4' + answer
            n = n // 3 - 1
        elif n % 3 == 1:
            answer = '1' + answer
            n = n // 3
        else:
            answer = '2' + answer
            n = n // 3

    print(answer)
    return answer
