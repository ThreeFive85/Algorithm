# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = [int(i) for i in str(n)[::-1]]
    print(answer)
    return answer
