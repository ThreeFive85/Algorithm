# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/60058
# 참고 블로그 : https://johnyejin.tistory.com/124

def solution(p):
    answer = ''
    stack = []
    print(check(p))
    print(divide(p))
    while len(p) != 0:
        u, p = divide(p)
        if check(u):
            answer += u
        else:
            answer += '(' + solution(p) + ')' + reverse(u[1:-1])
            break
    print(answer)
    return answer


def check(p):
    stack = []
    for i in p:
        if i == "(":
            stack.append("(")
        elif i == ")":
            if not stack:
                return False
            else:
                stack.pop()
    return True


def divide(p):
    cnt = [0, 0]
    for i in p:
        if i == "(":
            cnt[0] += 1
        else:
            cnt[1] += 1
        if cnt[0] == cnt[1]:
            break
    return p[:sum(cnt)], p[sum(cnt):]


def reverse(v):
    temp = ''
    for i in v:
        if i == '(':
            temp += ')'
        else:
            temp += '('
    return temp
