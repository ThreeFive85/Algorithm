# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12981#

from collections import deque

# 덱을 사용하여 먼저 스택에 덱의 첫 번째를 넣고 서로 비교
# 스택의 길이와 현재 몇 번째 플레이어인지를 확인하는 것으로 플레이어 번호 초기화
# 플레이어를 한 바퀴씩 돌면 턴을 +1


def solution(n, words):
    answer = []
    player = 1
    turn = 1
    deq = deque(words)
    stack = []
    while len(deq) > 1:
        stack.append(deq.popleft())
        player += 1
        # print("stack : ", stack[-1][-1])
        # print("deq : ", deq[0][0])
        if len(stack) % n == 0:
            player = 1
            turn += 1
        if stack[-1][-1] != deq[0][0]:
            return [player, turn]
        elif deq[0] in stack:
            return [player, turn]
    # print(player)
    # print(turn)
    return [0, 0]
