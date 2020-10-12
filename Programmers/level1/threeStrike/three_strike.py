# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/68935

def solution(n):
    answer = 0
    three = ''
    while n > 0:
        three += str(n % 3)
        n = n // 3
    rev = three[::-1]
    for i in range(len(rev)):
        answer += int(rev[i]) * 3**i

    print(answer)
    return answer


solution(45)
