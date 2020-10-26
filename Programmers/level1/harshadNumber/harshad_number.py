# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    answer = True
    sum_digits = 0
    for d in str(x):
        sum_digits += int(d)
    if x % sum_digits != 0:
        return False
    return answer
