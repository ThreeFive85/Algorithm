# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12935

def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        arr.append(-1)

    print(arr)
    return arr
