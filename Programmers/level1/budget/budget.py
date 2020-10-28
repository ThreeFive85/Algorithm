# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    d = sorted(d)
    for cost in d:
        if budget < cost:
            break
        else:
            budget -= cost
            answer += 1
    print(answer)
    return answer
