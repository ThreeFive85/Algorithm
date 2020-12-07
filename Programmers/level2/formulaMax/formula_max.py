# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/67257
# 참고 블로그 : https://eda-ai-lab.tistory.com/509
# 파이썬 정규식 레퍼런스 : https://python.flowdas.com/library/re.html
# 파이썬 permutation 레퍼런스 : https://python.flowdas.com/library/itertools.html?highlight=permutation#itertools.permutations

from itertools import permutations
import re


def solution(expression):
    answer = 0
    op = [x for x in ['*', '+', '-'] if x in expression]
    # print(op)
    op = [list(x) for x in permutations(op)]
    # print("op : ", op)
    exp = re.split(r'(\D)', expression)
    # print("exp : ", exp)
    stack = []
    for x in op:
        ex = exp[:]  # 새로운 배열로 복사
        # print("ex : ", ex)
        for y in x:
            # print(y)
            while y in ex:
                tmp = ex.index(y)
                # ex) 200 * 300
                ex[tmp-1] = str(eval(ex[tmp-1]+ex[tmp]+ex[tmp+1]))
                ex = ex[:tmp]+ex[tmp+2:]  # 연산 한 것은 제거
        # print("stack : ", stack)
        stack.append(ex[-1])
    print("result stack : ", stack)
    return max(abs(int(x)) for x in stack)
