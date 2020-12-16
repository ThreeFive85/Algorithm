# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    while True:
        same_set = same(m, n, board)
        # print(same_set)
        if len(same_set) == 0:
            break
        for pad in same_set:  # 지워진 블록들을 '0'으로 교체
            board[pad[0]] = board[pad[0]][:pad[1]] + \
                '0' + board[pad[0]][pad[1]+1:]
        # print(board)
        # 블록이 지워지면 그 위 블록들은 내려가므로 해당 문자의 밑열에 '0'이 있으면 서로 교체
        # while문으로 중간에 '0'이 없어질 때 까지 반복
        cnt = len(board[0])
        while cnt > 1:
            for i in range(len(board)-1):
                for j in range(len(board[i])):
                    if board[i+1][j] == '0':
                        char = board[i][j]
                        board[i] = board[i][:j] + '0' + board[i][j+1:]
                        board[i+1] = board[i+1][:j] + char + board[i+1][j+1:]
            cnt -= 1

    print(board)
    print(''.join(board).count('0'))
    return ''.join(board).count('0')


def same(x, y, pad):  # 같은 문자들의 좌표를 배열에 넣음 중복 값이 있으므로 set으로 중복값 제거
    arr = []
    for i in range(x-1):
        for j in range(y-1):
            if pad[i][j] == pad[i][j+1] and pad[i][j] == pad[i+1][j] and pad[i][j] \
                    == pad[i+1][j+1] and pad[i][j].isalpha():
                arr.append((i, j))
                arr.append((i, j+1))
                arr.append((i+1, j))
                arr.append((i+1, j+1))

    return set(arr)
