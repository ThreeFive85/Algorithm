# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = ""
    cnt = 0
    for spell in s:
        if cnt % 2 != 0:
            answer += spell.lower()
            cnt += 1
        elif spell == " ":
            answer += spell
            cnt = 0
        else:
            answer += spell.upper()
            cnt += 1
    print(answer)
    return answer
