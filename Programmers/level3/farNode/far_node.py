# https://programmers.co.kr/learn/courses/30/lessons/49189
# 참고 블로그 : https://jiwon-coding.tistory.com/112

from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[]*n for _ in range(n+1)]  # graph = [[], [], [], [], [], [], []]
    # graph의 index는 각 노드, graph[노드]는 노드와 연결된 노드들 ex) 1번 노드는 2, 3 노드들과 연결,
    #                                                         2번 노드는 1, 3, 4, 5노드들과 연결
    # test case graph = [[], [3, 2], [3, 1, 4, 5], [6, 4, 2, 1], [3, 2], [2], [3]]
    for a, b in edge:
        # print(f'a : {a}, b : {b}')
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (n+1)  # [0, 0, 0, 0, 0, 0, 0]
    visited[1] = 1  # [0, 1, 0, 0, 0, 0, 0]
    print(visited)
    que = deque([1])
    while(que):
        n = que.popleft()

        for i in graph[n]:
            if visited[i] == 0:
                que.append(i)
                visited[i] = visited[n] + 1
    answer = visited.count(max(visited))
    return answer


# solution(6, [[3, 6], [4, 3], [3, 2], [1, 3],
#          [1, 2], [2, 4], [5, 2]])  # return 3
