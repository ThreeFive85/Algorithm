# 문제 출처 : https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline

n = int(input())
result = []
for i in range(n):
    order = list(input().split())
    if order[0] == "push":
        result.append(int(order[1]))
    if order[0] == "pop":
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
            result.pop()
    if order[0] == "size":
        print(len(result))
    if order[0] == "empty":
        if len(result) == 0:
            print(1)
        else:
            print(0)
    if order[0] == "top":
        if len(result) == 0:
            print(-1)
        else:
            print(result[-1])
