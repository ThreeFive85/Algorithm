# 문제 출처 : https://www.acmicpc.net/status?user_id=threefive&problem_id=9012&from_mine=1

'''
해결 아이디어
    문자열을 돌면서 '('가 나오면 새로운 배열에 푸시를 하고 ')'일땐 새로운 배열에서 팝을 한다.
    그리고 최종적으로 남는 배열의 길이가 0이면 모두 '()'을 맞아 떨어지므로 YES를 출력하고
    아니면 NO를 출력한다.
'''

n = int(input())


def solution(p):
    check = []
    for i in p:
        if i == '(':
            check.append(i)
        else:
            if not check:
                print('NO')
                return
            else:
                check.pop()

    if len(check) == 0:
        print('YES')
        return
    else:
        print('NO')
        return


for _ in range(n):
    p = input()
    solution(p)


# solution('(())())')
# solution('(()())((()))')
