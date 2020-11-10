# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/62048

from math import gcd


def solution(w, h):
    print(w * h - (w + h - gcd(w, h)))
    return w * h - (w + h - gcd(w, h))
