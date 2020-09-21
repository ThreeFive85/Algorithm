# 문제 출처 : https://www.acmicpc.net/problem/1021

from sys import stdin
from collections import deque

n, p = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
deque = deque([i for i in range(1, n+1)])

count = 0

for num in arr:
    if deque[0] == num:
        deque.popleft()
        continue

    left_move = deque.index(num)
    right_move = len(deque) - left_move

    if left_move <= right_move:
        deque.rotate(-left_move)
        deque.popleft()
        count += left_move
    else:
        deque.rotate(right_move)
        deque.popleft()
        count += right_move

print(count)
