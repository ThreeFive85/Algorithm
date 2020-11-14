# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/68645
# 참고 블로그 : https://inspirit941.tistory.com/entry/Python-프로그래머스-삼각-달팽이-Level-2
# chain 사용법 : https://python.flowdas.com/library/itertools.html

from itertools import chain


def solution(n):
    maps = [[0 for _ in range(n)] for _ in range(n)]
    y, x = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:  # 아래로 이동
                y += 1
            elif i % 3 == 1:  # 오른쪽으로 이동
                x += 1
            elif i % 3 == 2:  # 위로 이동
                y -= 1
                x -= 1
            maps[y][x] = num
            num += 1
    answer = [i for i in chain(*maps) if i != 0]

    print(answer)
    return answer
