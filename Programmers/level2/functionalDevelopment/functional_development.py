# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
# 참고 블로그 : https://geonlee.tistory.com/122

import math


def solution(progresses, speeds):
    answer = []
    # 각 작업별로 완료되기까지(>100) 걸리는 시간에 데이터를 하나의 리스트로
    progresses = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    front = 0
    for i in range(len(progresses)):
        if progresses[front] < progresses[i]:
            answer.append(i - front)
            front = i
    answer.append(len(progresses) - front)
    print(answer)
    return answer


solution([93, 30, 55], [1, 30, 5])
