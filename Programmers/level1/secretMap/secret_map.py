# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = forArr(arr1)
    bin_arr2 = forArr(arr2)

    for i in range(n):
        result = ''
        for j in range(n):
            if bin_arr1[i][j] == '0' and bin_arr2[i][j] == '0':
                result += ' '
            else:
                result += '#'
        answer.append(result)
    print(answer)
    return answer

# 이진수 변환


def binary(n, arr_length):
    trans = ''
    while n > 0:
        trans += str(n % 2)
        n = n // 2
    if arr_length > len(trans):
        p = arr_length - len(trans)
        while p > 0:
            trans += '0'
            p -= 1

    return trans[::-1]

# for문을 돌면서 이진수로 변환하여 배열에 넣음


def forArr(arr):
    nums = []
    for n in arr:
        bina = binary(n, len(arr))
        nums.append(bina)

    return nums
