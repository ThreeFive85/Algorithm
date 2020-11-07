# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    de_truck_weights = deque(truck_weights)
    de_bridge = deque([0] * bridge_length)
    de_bridge[-1] = de_truck_weights.popleft()
    current_weight = de_bridge[-1]
    # print(de_truck_weights)
    # print(de_bridge)

    while de_truck_weights:
        if current_weight - de_bridge[0] + de_truck_weights[0] > weight:
            current_weight -= de_bridge[0]
            de_bridge.popleft()
            de_bridge.append(0)
            answer += 1
        else:
            current_weight += de_truck_weights[0]
            current_weight -= de_bridge[0]
            de_bridge.popleft()
            de_bridge.append(de_truck_weights.popleft())
            answer += 1

    print(answer + bridge_length)
    return answer + bridge_length
