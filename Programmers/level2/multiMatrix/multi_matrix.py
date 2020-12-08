# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([])
        for j in range(len(arr2[0])):
            answer[i].append(0)
    # print(answer)
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer


'''
zip을 사용해 행을 열로 바꾸어 연산하는 다른 코드 내용
참고 : https://programmers.co.kr/learn/courses/30/lessons/12949/solution_groups?language=python3
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
'''
