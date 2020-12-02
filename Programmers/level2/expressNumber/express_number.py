# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 1
    for i in range(1, n//2 + 2):
        plus = i
        for j in range(i + 1, n//2 + 2):
            plus += j
            if plus == n:
                answer += 1
                break
            elif plus > n:
                break
            else:
                continue
    return answer
