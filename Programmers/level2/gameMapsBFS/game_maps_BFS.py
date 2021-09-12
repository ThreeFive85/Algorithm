# https://programmers.co.kr/learn/courses/30/lessons/1844?language=python3
# 참고 블로그 : https://jokerldg.github.io/algorithm/2021/05/23/game-map.html
# https://velog.io/@fftl/프로그래머스-게임-맵-최단거리-파이썬

from collections import deque


def solution(maps):
    answer = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    r = len(maps)
    c = len(maps[0])
    table = [[-1 for _ in range(c)] for _ in range(r)]
    table[0][0] = 1
    que = deque([[0, 0]])
    while que:
        y, x = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
                if table[ny][nx] == -1:
                    table[ny][nx] = table[y][x] + 1
                    que.append([ny, nx])
                # print("table : ", table)
                # print("que : ", que)
    answer = table[-1][-1]
    return answer
