# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12940

from math import gcd


def solution(n, m):
    return [gcd(n, m), n*m/gcd(n, m)]


'''
참고 블로그 : https://dimenchoi.tistory.com/46

유클리드 호제법

def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
'''
