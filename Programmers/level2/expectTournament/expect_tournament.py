# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12985#

# a, b가 1, 2일때 서로 동일한 값으로 만들어 준다. 루프로 동일한 값이 될 때까지 반복
def solution(n, a, b):
    answer = 0

    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2
        print(f'현재 a {a}, b {b}')
    # print(answer)
    return answer
