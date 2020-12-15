# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12973

from collections import deque


def solution(s):
    deq = deque(list(s))
    # print(deq)
    stack = []
    while deq:
        stack.append(deq.popleft())
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
    # print(stack)
    if len(stack) == 0:
        return 1
    else:
        return 0
