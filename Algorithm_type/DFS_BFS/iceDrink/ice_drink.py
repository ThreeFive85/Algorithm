# 문제 : https://www.youtube.com/watch?v=e7_H8SLZlHY&t=826s&ab_channel=한빛미디어

# 음료수 얼려 먹기

# N * M 크기의 얼음 틀이 있다. 구멍이 뚫려 있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주
# 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하라

# 예시) input: [[0,0,1,1,0], [0,0,0,1,1], [1,1,1,1,1], [0,0,0,0,0]]
#           00110
#           00011
#           11111
#           00000
# result : 3

# DFS를 활용
# 1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 0이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문
# 2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복하면, 연결된 모든 지점을 방문할 수 있다.
# 3. 모든 노드에 대하여 1번, 2번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트

def solution(ice):
    result = 0
    for i in range(len(ice)):
        for j in range(len(ice[0])):
            if dfs(ice, i, j, len(ice), len(ice[0])) == True:
                result += 1
    print(result)
    return result


def dfs(graph, x, y, n, m):
    # 주어진 범위를 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들을 재귀적으로 수행
        dfs(graph, x-1, y, n, m)
        dfs(graph, x, y-1, n, m)
        dfs(graph, x+1, y, n, m)
        dfs(graph, x, y+1, n, m)
        return True
    return False


solution([[0, 0, 1, 1, 0], [0, 0, 0, 1, 1],
          [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]])
