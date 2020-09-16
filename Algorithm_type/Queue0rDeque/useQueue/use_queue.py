from sys import stdin
from collections import deque

# que = deque()

# que.append(1)
# que.append(2)
# print(que[0])

n = int(stdin.readline())

que = deque()

for i in range(n):
    x = list(stdin.readline().split())

    if 'push' in x:
        que.append(int(x[1]))
        print(que)
    elif 'pop' in x:
        if not deque:
            print(-1)
        else:
            print(que.popleft())
    elif 'size' in x:
        print(len(que))
    elif 'empty' in x:
        if len(que) != 0:
            print(0)
        else:
            print(-1)
    elif 'front' in x:
        if len(que) != 0:
            print(que.popleft())
        else:
            print(-1)
    elif 'back' in x:
        if len(que) != 0:
            print(que.pop())
        else:
            print(-1)
