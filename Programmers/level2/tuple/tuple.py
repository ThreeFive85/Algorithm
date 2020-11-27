# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/64065

import re


def solution(s):
    answer = []
    p = s.split(",{")
    p.sort(key=len)
    for k in p:
        numbers = re.findall("\d+", k)  # 문자열 안에 정수만 추출하는 정규식
        for n in numbers:
            if int(n) not in answer:
                answer.append(int(n))
    return answer
