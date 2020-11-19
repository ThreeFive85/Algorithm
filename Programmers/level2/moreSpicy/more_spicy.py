# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    print(type(scoville))
    while True:
        if scoville[0] >= K:
            break
        elif len(scoville) <= 1 and scoville[0] < K:
            answer = -1
            break
        num = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, num)
        answer += 1
    return answer
