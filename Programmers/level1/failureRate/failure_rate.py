# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = {}
    users = len(stages)
    for i in range(1, N+1):
        if users != 0:
            answer[i] = stages.count(i) / users
            users -= stages.count(i)
        else:
            answer[i] = 0

    print(answer)
    print(sorted(answer, key=lambda x: answer[x], reverse=True))
    return sorted(answer, key=lambda x: answer[x], reverse=True)


'''
런타임 에러 코드
from operator import itemgetter
def solution(N, stages):
    answer = []
    failed = []
    users = len(stages)
    for i in range(1, N+1):
        failed.append((i, stages.count(i)/users))
        users -= stages.count(i)
    print(sorted(failed, key=itemgetter(1), reverse=True))
    sort_failed = sorted(failed, key=itemgetter(1), reverse=True)
    for i in range(len(sort_failed)):
        answer.append(sort_failed[i][0])
    return answer

유저가 0일때를 제외해야 하는 듯
'''
