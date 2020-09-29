# BFS(Breadth First Search, 너비 우선 탐색)

BFS는 너비를 우선해서 그래프를 탐색하는 기법이다. 시작점인 루트 노드와 같은 거리에 있는 노드를 우선으로 방문한다.  
일반적으로 큐 자료구조를 사용하여 노드를 방문하면서 인접한 노드 중 방문하지 않았던 노드의 정보만 큐에 넣어 먼저 큐에  
들어있던 노드부터 방문하면 되는 것이다.  
파이썬에서는 collections 라이브러리의 deque를 사용하면 시간을 절약할 수 있다.  
또한 인접 노드 중 방문하지 않았던 노드를 큐에 넣을 때는 파이썬 데이터 타입 중 set을 사용하면 쉽게 구현할 수 있다.  
만약 다음과 같은 방향이 있는 유향 그래프를 BFS로 탐색한다면,

```py
graph_list = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
root_node = 1
```

구현

```py
def BFS_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

print(BFS_with_adj_list(graph_list, root_node))
```

# DFS(Depth First Search, 깊이 우선 탐색)

DFS는 한 방향으로 갈 수 있을 만큼 깊게 탐색하는 방식이다.  
갈 수 있는 한 끝까지 탐색해 리프 노드를 방문하고, 이전 갈림길에서 선택하지 않았던 노드를 방문하는 식으로  
탐색을 한다.  
일반적으로 스택 자료구조를 사용한다.

구현

```py
def DFS_with_adj_list(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

print(DFS_with_adj_list(graph_list, root_node))
```
