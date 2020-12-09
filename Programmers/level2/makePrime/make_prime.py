# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations
import math


def solution(nums):
    answer = 0
    per = list(combinations(nums, 3))
    # print(per)
    for i in range(len(per)):
        if prime(per[i]) == True:
            answer += 1
    return answer


def prime(arr):
    # print(sum(arr))
    if sum(arr) <= 0 or sum(arr) % 1 != 0:
        return False
    elif sum(arr) == 1:
        return False
    else:
        num = math.sqrt(sum(arr))
        for i in range(2, int(num+1)):
            if sum(arr) % i == 0:
                return False
    return True


print(prime([1, 2, 3]))
