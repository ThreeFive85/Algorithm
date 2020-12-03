# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    a = list(map(int, s.split(" ")))
    print(a)
    return f'{min(a)} {max(a)}'
