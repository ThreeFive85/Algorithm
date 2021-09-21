# https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3
# 참고 블로그: https://gurumee92.tistory.com/164

def solution(N, number):
    # 마지막 테스트 케이스
    if N == number:
        return 1

    answer = 0
    # s = [set(), set(), set(), set(), set(), set(), set(), set()]
    s = [set() for x in range(8)]
    # s = [{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        # print(f'현재 s[{j}] : {s[j]}')
        if number in s[i]:
            answer = i + 1
            break
    else:
        answer = -1
    return answer


# solution(5, 1)  # return 4
