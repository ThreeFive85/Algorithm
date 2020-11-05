# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]

    print(arr1)
    return arr1

# zip 함수
# 참고 레퍼런스 : https://wikidocs.net/32#zip

# def solution(A, B):
#     return [[c + d for c, d in zip(a, b)] for a, b in zip(A, B)]
