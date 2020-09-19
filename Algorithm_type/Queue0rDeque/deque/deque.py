# 문제 출처 : https://www.acmicpc.net/problem/10866

from sys import stdin
from collections import deque

n = int(stdin.readline())
deque = deque()


def push_front(deque, x):
    deque.appendleft(x)


def push_back(deque, x):
    deque.append(x)


def pop_front():
    if not deque:
        return(-1)
    else:
        return(deque.popleft())


def pop_back():
    if not deque:
        return(-1)
    else:
        return(deque.pop())


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

    if x[0] == 'push_front':
        push_front(deque, int(x[1]))
    elif x[0] == 'push_back':
        push_back(deque, int(x[1]))
    elif x[0] == 'pop_front':
        print(pop_front())
    elif x[0] == 'pop_back':
        print(pop_back())
    elif x[0] == 'size':
        print(size())
    elif x[0] == 'empty':
        print(empty())
    elif x[0] == 'front':
        print(front())
    elif x[0] == 'back':
        print(back())
