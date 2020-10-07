# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):

    answer = sorted(sorted(strings), key=lambda string: string[n])

    return answer
