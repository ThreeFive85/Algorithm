# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12953

from math import gcd


def solution(arr):
    while len(arr) > 1:
        num = lcm(arr.pop(), arr.pop())
        arr.append(num)
    print(num)
    return num


def lcm(a, b):
    return int(a * b / gcd(a, b))

# print(lcm(2,3))
