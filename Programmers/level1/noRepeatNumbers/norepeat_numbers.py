# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
        elif answer[-1] == arr[i]:
            continue
        else:
            answer.append(arr[i])
    return answer

# def solution(s):
#     a = []
#     for i in s:
#         if a[-1:] == [i]:
#             continue
#         a.append(i)

#     print(a)
#     return a


# solution([4, 4, 4, 3, 3])
