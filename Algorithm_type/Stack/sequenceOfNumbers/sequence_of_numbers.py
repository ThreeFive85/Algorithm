# 문제 출처 : https://www.acmicpc.net/problem/1874
# 참고 블로그 : https://assaeunji.github.io/python/2020-05-04-bj1874/,
#            https://chancoding.tistory.com/33

# n = int(input())

# stack = []
# result = []
# cnt = 0
# no_massage = True

# for i in range(0,n):
#     x = int(input())
#     while cnt < x:
#         cnt += 1
#         stack.append(cnt)
#         result.append('+')

#     if stack[-1] == x:
#         stack.pop()
#         result.append('-')

#     else:
#         no_massage = False
#         exit(0)

# if no_massage == False:
#     print('NO')
# else:
#     print('\n'.join(result))
# 위 코드로 진행시 백준알고리즘 테스트에서는 시간도 오래 걸리고 오답 처리로 된다.

import sys

n = int(sys.stdin.readline())
p = map(lambda x: int(x.rstrip()), sys.stdin.readlines())


def solution():
    stack, result, cnt = [], [], 1
    for i in p:
        while cnt <= i:
            stack.append(cnt)
            result.append('+')
            cnt += 1
        if stack.pop() != i:
            return 'NO'
        else:
            result.append('-')
    return '\n'.join(result)


print(solution())
