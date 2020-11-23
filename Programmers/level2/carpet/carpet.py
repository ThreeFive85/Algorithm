# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    total = brown + yellow
    for i in range(1, total+1):
        if total % i == 0:
            x = total // i
            y = i
            if x < y:
                break
            else:
                answer.append([x, y])
    # print(answer)

    for i in answer:
        if i[0] * 2 + i[1] * 2 - 4 == brown:
            return i
