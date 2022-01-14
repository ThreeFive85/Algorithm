# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    answer = []
    board = []
    num = 1
    for i in range(rows):
        arr = []
        for j in range(columns):
            arr.append(num)
            num += 1
        board.append(arr)
    # print(board)
    for q in queries:
        location = [x-1 for x in q]
        x1, y1, x2, y2 = location
        tmp = board[x1][y1]
        s = tmp
        # print(tmp)
        # left
        for i in range(x1+1, x2+1):
            board[i-1][y1] = board[i][y1]
            s = min(s, board[i][y1])
        # bottom
        for i in range(y1+1, y2+1):
            board[x2][i-1] = board[x2][i]
            s = min(s, board[x2][i])
        # right
        for i in range(x2-1, x1-1, -1):
            board[i+1][y2] = board[i][y2]
            s = min(s, board[i][y2])
        # top
        for i in range(y2-1, y1-1, -1):
            board[x1][i+1] = board[x1][i]
            s = min(s, board[x1][i])

        board[x1][y1+1] = tmp

        answer.append(s)

        # print(board)
    return answer
