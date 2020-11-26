# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12905
# 참고 블로그 : https://velog.io/@tjdud0123/가장-큰-정사각형
# DP(Dynamic programming, 동적 계획법) 유형 문제

from itertools import chain


def solution(board):
    m, n = len(board), len(board[0])
    for i in range(1, m):
        for j in range(1, n):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i-1]
                                  [j], board[i][j-1]) + 1
    # print(board)
    # print(list(chain(*board)))
    return max(chain(*board))**2
