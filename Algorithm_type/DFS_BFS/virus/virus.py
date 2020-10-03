# 문제 출처 : https://www.acmicpc.net/problem/2606

# coms = [[1, 2], [2, 3], [1, 5], [5, 2], [5, 6], [4, 7]]
from sys import stdin
from collections import deque
''' 
n = int(stdin.readline())
p = int(stdin.readline())
coms = []
result = [1]
for i in range(p):
    network = list(map(int, stdin.readline().split()))
    coms.append(network)

for i in range(len(coms)):
    for j in range(len(coms[i])):
        if coms[i][j] in result:
            for k in range(len(coms[i])):
                if coms[i][k] in result:
                    continue
                else:
                    result.append(coms[i][k])
# print(result)
result.pop(0)
print(len(result))
이렇게 풀어 보았지만 정답과는 맞지 않음 
'''

'''
def BFS(graph):
    visited = []
    queue = deque([1])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
            # queue.extend(graph[n])
    return visited


def virus():
    answer = 0
    n = int(stdin.readline())
    p = int(stdin.readline())
    graph = [set() for _ in range(n+1)]
    for _ in range(p):
        i, j = map(int, stdin.readline().split())
        graph[i].add(j)
        graph[j].add(i)

    result = BFS(graph)
    print(len(result) - 1)


virus()
위 코드에서는 vscode에서는 잘 동작하는데 백준에서는 런타임 에러. 왜지
'''

dic = {}
for i in range(int(stdin.readline())):
    dic[i+1] = set()
# print(dic)
for j in range(int(stdin.readline())):
    a, b = map(int, stdin.readline().split())
    dic[a].add(b)
    dic[b].add(a)
print(dic)
visited = []


def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


bfs(1, dic)
print(visited)
print(len(visited) - 1)
