# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    prize = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    max_cnt = 0
    min_cnt = 0
    for num in lottos:
        if num in win_nums:
            max_cnt += 1
            min_cnt += 1
        elif num == 0:
            max_cnt += 1

    answer = [prize[max_cnt], prize[min_cnt]]
    return answer
