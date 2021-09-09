# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/84325

def solution(table, languages, preference):
    arr = []
    for jobs in table:
        job = jobs.split(' ')
        lang_num = 0
        for i in range(len(languages)):
            if languages[i] not in job:
                lang_num += 0
            else:
                lang_num += preference[i] * (6 - job.index(languages[i]))
        arr.append((job[0], lang_num))
    # print(arr)

    # -x[1]는 높은숫자로 내림차순, x[0]은 사전 순으로 오름차순
    arr.sort(key=lambda x: (-x[1], x[0]))

    # print(arr)
    return arr[0][0]
