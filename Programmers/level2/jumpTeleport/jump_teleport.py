# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    ans = 1
    # print(bin(n))
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            n = n // 2
        else:
            n = (n-1) // 2
            ans += 1
    return ans

# n을 이진수로 변경하여 1의 갯수를 리턴하는 방법도 가능하다.
