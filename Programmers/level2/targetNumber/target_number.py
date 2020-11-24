# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/43165
# 참고 블로그 : https://eda-ai-lab.tistory.com/475

# from itertools import product


# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     # print(l)
#     # print(list(product(*l)))
#     s = list(map(sum, product(*l)))
#     # print(s)
#     return s.count(target)

# bfs
from collections import deque


def solution(numbers, target):
    answer = 0
    stack = deque([(0, 0)])
    while stack:
        cur_sum, num_idx = stack.popleft()

        if num_idx == len(numbers):
            if cur_sum == target:
                answer += 1
        else:
            number = numbers[num_idx]
            stack.append((cur_sum+number, num_idx+1))
            stack.append((cur_sum-number, num_idx+1))

    print(answer)
    return answer


solution([1, 1, 1, 1, 1], 3)
