# https://programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    cnt = len(s)
    while cnt > 0:
        if check(s):
            answer += 1
        s = s[1:] + s[0]
        cnt -= 1
    return answer


def check(c):
    stack = []
    strObj = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    for char in c:
        if char == '[' or char == '(' or char == '{':
            stack.append(char)
        elif char == ']' or char == ')' or char == '}':
            if not stack:
                return False
            recent = stack.pop()
            if char != strObj[recent]:
                return False
    if len(stack) != 0:
        return False
    else:
        return True
