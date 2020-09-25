# 문제 출처 : https://www.acmicpc.net/problem/11047

from sys import stdin

n, p = map(int, stdin.readline().split())

coins = []

for i in range(n):
    coins.append(int(stdin.readline()))

coins.reverse()
cnt = 0
while p > 0:
    for i in range(len(coins)):
        if coins[i] > p:
            continue
        else:
            cnt += p//coins[i]
            p = p % coins[i]
print(cnt)
