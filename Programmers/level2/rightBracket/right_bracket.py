# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append("(")
        elif char == ")":
            if not stack:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
