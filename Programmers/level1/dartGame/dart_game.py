# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/17682

import re


def solution(dartResult):
    answer = 0
    scores = []
    num = ''
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for dart in dartResult:
        if dart == "S":
            scores.append(int(num))
            scores[-1] = scores[-1] ** 1
            num = ''
        elif dart == "D":
            scores.append(int(num))
            scores[-1] = scores[-1] ** 2
            num = ''
        elif dart == "T":
            scores.append(int(num))
            scores[-1] = scores[-1] ** 3
            num = ''
        elif dart == "*":
            if len(scores) > 1:
                scores[-1] = scores[-1] * 2
                scores[-2] = scores[-2] * 2
            else:
                scores[-1] = scores[-1] * 2
        elif dart == "#":
            scores[-1] = scores[-1] * -1
        else:
            num += dart
    print(scores)
    return sum(scores)


solution("1S2D*3T")

'''
다른 코드 : https://programmers.co.kr/learn/courses/30/lessons/17682/solution_groups?language=python3

import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
'''
