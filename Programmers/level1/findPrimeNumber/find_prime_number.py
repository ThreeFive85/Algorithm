# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12921

import math


def solution(n):
    answer = 0
    for i in range(1, n+1):
        if prime(i) == True:
            answer += 1
    return answer


def prime(n):
    if n <= 1 or n % 1 != 0:
        return False
    num = math.sqrt(n)
    for i in range(2, int(num+1)):
        if n % i == 0:
            return False
    return True


print(solution(10))
print(solution(5))
