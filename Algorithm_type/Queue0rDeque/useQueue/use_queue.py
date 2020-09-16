from sys import stdin
from collections import deque

n = int(stdin.readline())

deque = deque()


def push(deque, x):
    deque.append(x)


def pop():
    if not deque:
        return(-1)
    else:
        return(deque.popleft())


def size():
    return len(deque)


def empty():
    if not deque:
        return 1
    else:
        return 0


def front():
    if not deque:
        return -1
    else:
        return deque[0]


def back():
    if not deque:
        return -1
    else:
        return deque[-1]


for i in range(n):
    x = stdin.readline().split()

    if x[0] == "push":
        push(deque, int(x[1]))
    elif x[0] == 'pop':
        print(pop())
    elif x[0] == 'size':
        print(size())
    elif x[0] == 'empty':
        print(empty())
    elif x[0] == 'front':
        print(front())
    elif x[0] == 'back':
        print(back())

# for i in range(n):
#     x = list(stdin.readline().split())

#     if 'push' in x:
#         deque.append(int(x[1]))
#         print(deque)
#     elif 'pop' in x:
#         if not dedeque:
#             print(-1)
#         else:
#             print(deque.popleft())
#     elif 'size' in x:
#         print(len(deque))
#     elif 'empty' in x:
#         if len(deque) != 0:
#             print(0)
#         else:
#             print(-1)
#     elif 'front' in x:
#         if len(deque) != 0:
#             print(deque.popleft())
#         else:
#             print(-1)
#     elif 'back' in x:
#         if len(deque) != 0:
#             print(deque.pop())
#         else:
#             print(-1)
