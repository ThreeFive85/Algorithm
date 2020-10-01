# 문제 출처 : https://www.acmicpc.net/problem/2667

from sys import stdin

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(stdin.readline())
a = [list(stdin.readline().rstrip()) for _ in range(n)]

# print(a)

cnt = 0
apt = []


def dfs(x, y):
    global cnt
    a[x][y] = '0'  # 방문한 곳은 0으로
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        # print('nx : ', nx)
        ny = y + dy[i]
        # print('ny : ', ny)
        # print('----------------')
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if a[nx][ny] == '1':
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if a[i][j] == '1':
            cnt = 0
            dfs(i, j)
            apt.append(cnt)

print(len(apt))
# print(apt)
# print(a)
apt.sort()
for i in apt:
    print(i)
