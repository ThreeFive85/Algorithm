# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

from itertools import permutations
import math


def solution(numbers):
    answer = 0
    '''
    오류코드
    arr = list(map(int, list(numbers)))
    for per in permutations(list(numbers)):
        arr.append(int(''.join(per)))
    print(set(arr))
    배열에 제대로 순열이 안들어감
    '''
    new_numbers = list(numbers)
    for i in range(2, len(numbers)+1):
        per = list(permutations(numbers, i))
        for j in per:
            if len(j) <= len(numbers):
                new_numbers.append(''.join(j))
    # print(new_numbers)
    new_numbers = list(set([int(x) for x in new_numbers]))
    # print(new_numbers)
    for num in new_numbers:
        if primetester(num) == True:
            answer += 1
    return answer


def primetester(n):
    if n <= 0 or n % 1 != 0:
        return False
    elif n == 1:
        return False
    else:
        num = math.sqrt(n)
        for i in range(2, int(num + 1)):
            if n % i == 0:
                return False
    return True
