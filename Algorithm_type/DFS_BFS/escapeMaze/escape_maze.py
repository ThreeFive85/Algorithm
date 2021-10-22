# 문제 : https://www.youtube.com/watch?v=e7_H8SLZlHY&t=826s&ab_channel=한빛미디어

# 미로 탈출
# 유저는 N * M 크기의 직사각형 형태의 미로에 갇혔다. 미로에는 괴물들이 존재하고 이를 피해 탈출해야 한다.
# 유저의 시작 위치는 (1,1)이며 출구는 (N,M)의 위치에 존재하고 한 번에 한 칸씩 이동할 수 있다.
# 괴물이 있는 부분은 0, 없는 부분은 1로 표시된다. 미로는 반드시 탈출 할 수 있는 형태로 주어진다.
# 이때 유저가 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하여라. 시작점과 마지막점도 포함되어야 한다.

# 예시) input: [[1,0,1,0,1,0], [1,1,1,1,1,1], [0,0,0,0,0,1], [1,1,1,1,1,1], [1,1,1,1,1,1]]

#             101010
#             111111
#             000001
#             111111
#             111111

# result = 10

from collections import deque


def solution(maze):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        # print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(maze) or ny < 0 or ny >= len(maze[0]):
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx, ny))

    # print(maze)

    return maze[len(maze)-1][len(maze[0])-1]


solution([[1, 1, 1], [1, 0, 1], [0, 0, 1]])
