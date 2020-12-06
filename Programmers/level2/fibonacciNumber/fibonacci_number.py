# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12945

def solution(n):
    answer = 0
    stack = [0, 1]
    if n > 2:
        for i in range(2, n+1):
            stack.append(stack[i-1]+stack[i-2])
    num = stack[-1]
    print(stack)
    return num % 1234567


# solution(50)
# solution(150)

'''
def recu(n):
    if n <= 2:
        return 1
    print(recu(n-1) + recu(n-2))
    return recu(n-1) + recu(n-2)

피보나치수열을 재귀함수로 만들면 n의 수가 조금만 높아져도 연산이 많아져 느려진다
시간복잡도 2^n
recu(50)
'''
