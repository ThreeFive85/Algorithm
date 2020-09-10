# 문제 출처 : https://www.acmicpc.net/problem/10773

# 리스트를 돌며 새로운 배열에 숫자를 담는데 0일때는 마지막에 들어온 숫자를 지운다.

from sys import stdin
n = int(input())
p = list(map(int, stdin.read().split()))

new_list = []
result = 0
for i in range(len(p)):
    if p[i] == 0:
        new_list.pop()
    else:
        new_list.append(p[i])
result = sum(new_list)
print(result)
