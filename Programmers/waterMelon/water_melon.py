# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12922

def solution(n):
    answer = '수'
    for i in range(1, n):
        if n == 1:
            return answer
        if answer[i-1] == '수':
            answer += '박'
        if answer[i-1] == '박':
            answer += '수'
    print(answer)
    return answer

# def water_melon(n):

#     answer = "수박" * n

#     return answer[:n]
