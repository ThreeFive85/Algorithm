# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    answer = [x]
    while n > 1:
        answer.append(answer[-1] + x)
        n -= 1
    print(answer)
    return answer

# def solution(x, n):
#     return [(i*x)+x for i in range(n)]
