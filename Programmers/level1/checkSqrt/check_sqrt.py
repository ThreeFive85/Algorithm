# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12934

import math


def solution(n):
    answer = 0
    if n % math.sqrt(n) == 0:
        answer = (math.sqrt(n)+1) ** 2
        print(answer)
        return answer
    else:
        return -1

# math을  import하지 않아도 sqrt = n ** (1/2)로 제곱근을 구할 수 있다.
