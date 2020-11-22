# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42885#
# 참고 블로그 : https://eda-ai-lab.tistory.com/474

from collections import deque


def solution(people, limit):
    answer = 0
    people.sort()
    deq = deque(people)
    ran = len(deq)
    while ran != 0:
        wei = 0
        pop = deq.pop()
        lim = limit
        ran -= 1
        wei += pop
        lim -= pop
        if len(deq) >= 1:
            if lim >= deq[0]:
                deq.popleft()
                ran -= 1
        answer += 1
    return answer
