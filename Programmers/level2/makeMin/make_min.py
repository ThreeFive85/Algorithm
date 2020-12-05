# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    answer = 0
    sort_a = sorted(A)
    sort_b = sorted(B, reverse=True)
    for i in range(len(A)):
        num = sort_a[i] * sort_b[i]
        answer += num
    return answer
