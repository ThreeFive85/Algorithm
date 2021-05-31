# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/76501?language=python3

def solution(absolutes, signs):
    answer = 0
    for i in range(len(signs)):
        if signs[i] == False:
            answer += -absolutes[i]
        else:
            answer += absolutes[i]

    return answer
