# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []
    users = {}
    for reco in record:
        user = reco.split(' ')
        if user[0] == 'Enter':
            users[user[1]] = user[2]
        if user[0] == "Change":
            users[user[1]] = user[2]
    # print(users)
    for reco in record:
        user = reco.split(' ')
        if user[0] == "Enter":
            answer.append(f'{users[user[1]]}님이 들어왔습니다.')
        if user[0] == "Leave":
            answer.append(f'{users[user[1]]}님이 나갔습니다.')
    # print(answer)
    return answer
