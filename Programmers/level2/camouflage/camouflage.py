# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3

from functools import reduce


def solution(clothes):
    obj = {}
    for i in range(len(clothes)):
        if clothes[i][1] in obj:
            obj[clothes[i][1]] += 1
        else:
            obj[clothes[i][1]] = 1
    print(obj)
    answer = reduce(lambda x, y: x*(y+1), obj.values(), 1) - 1
    return answer
