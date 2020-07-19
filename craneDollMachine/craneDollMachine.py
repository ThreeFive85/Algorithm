'''
board
[
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]

moves
[1,5,3,5,1,2,1,4]

result 4
'''


def solution(board, moves):
    answer = []
    stack = []

    for move in moves:
        move = move - 1
        for i in range(len(board)):
            if board[i][move] != 0:
                stack.append(board[i][move])
                board[i][move] = 0
                if stack[-1:] == stack[-2:-1]:
                    answer += stack[-1:]
                    stack = stack[:-2]
                break
    # print(answer)
    print(len(answer) * 2)
    return len(answer) * 2
    # print("stack[-1:] : ", stack[-1:])
    # print("stack[-2:-1] : ", stack[-2:-1])


solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
         4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])
