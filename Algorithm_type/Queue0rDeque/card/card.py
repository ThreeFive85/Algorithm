# 문제 출처 : https://www.acmicpc.net/problem/2164

from sys import stdin
from collections import deque

n = int(stdin.readline())

deque = deque()

for i in range(1, n+1):
    deque.append(i)

while len(deque) > 1:
    deque.popleft()
    deque.append(deque.popleft())
print(deque[0])
