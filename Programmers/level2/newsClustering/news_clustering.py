# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/17677

import math


def solution(str1, str2):
    answer = 0
    div1 = [str1[i:i+2].upper() for i in range(len(str1))
            if len(str1[i:i+2]) == 2 and str1[i:i+2].isalpha()]
    # print(div1)
    div2 = [str2[i:i+2].upper() for i in range(len(str2))
            if len(str2[i:i+2]) == 2 and str2[i:i+2].isalpha()]
    inter = set(div1) & set(div2)
    # print("교집합: ", inter)
    union = set(div1) | set(div2)
    # print("합집합: ", union)
    if len(union) == 0:
        return 65536
    # 교집합과 합집합의 카운트를 따로 계산
    inter_sum = sum([min(div1.count(gyo), div2.count(gyo)) for gyo in inter])
    uni_sum = sum([max(div1.count(hap), div2.count(hap)) for hap in union])
    # print(inter_sum)

    return math.floor((inter_sum/uni_sum)*65536)
