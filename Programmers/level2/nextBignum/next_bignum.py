# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0
    cnt = binary(n).count("1")
    p = 1
    next_num = binary(n+p)
    while True:
        if cnt == next_num.count("1"):
            break
        else:
            p += 1
            next_num = binary(n+p)
    print(change(next_num))
    return change(next_num)


def binary(n):  # 이진수 변환
    result = ''
    while n > 0:
        rest = n % 2
        result += str(rest)
        n = n // 2
    # print(result[::-1])
    return result
# binary(78)
# binary(15)


def change(n):  # 이진수를 정수로
    result = 0
    for i in range(len(n)):
        if n[i] == "0":
            result += 0
        else:
            result += 2 ** int(i)
    # print(result)
    return result
# change('0111001')
# change('1111')


'''
다른 풀이

def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n

python 함수 중 bin()을 사용하여 이진법으로 바로 변환 가능
'''
