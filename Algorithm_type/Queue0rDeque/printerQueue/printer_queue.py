# 문제 출처 : https://www.acmicpc.net/problem/1966

from sys import stdin
test = int(stdin.readline())

for i in range(test):
    n, idx = map(int, stdin.readline().split())
    arr = list(map(int, stdin.readline().split()))

    m = max(arr)
    count = 0

    while True:
        first = arr.pop(0)
        if first == m:
            count += 1
            if idx == 0:
                break
            else:
                idx -= 1
            m = max(arr)
        else:
            arr.append(first)
            if idx == 0:
                idx = len(arr) - 1
            else:
                idx -= 1

    print(count)
