# https://programmers.co.kr/learn/courses/30/lessons/87946?language=python3

import itertools


def solution(k, dungeons):
    arr = []
    per = list(itertools.permutations(dungeons, len(dungeons)))
    # print(per)
    for p in per:
        r = result(p, k)
        arr.append(r)
    # print(arr)
    return max(arr)


def result(arr, k):
    answer = 0
    for a in arr:
        if a[0] <= k:
            k -= a[1]
            answer += 1
    return answer
