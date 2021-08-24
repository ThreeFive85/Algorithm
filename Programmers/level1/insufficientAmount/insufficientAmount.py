# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):

    need = 0
    for i in range(1, count+1):
        need += price*i
    print(need)
    if need <= money:
        return 0
    return need - money
