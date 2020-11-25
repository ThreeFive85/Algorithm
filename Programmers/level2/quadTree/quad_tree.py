# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/68936
# 참고 블로그 : https://goodlucknua.tistory.com/76, https://jinomadstory.tistory.com/45

def solution(arr):
    answer = []

    def recu(x, y, n):
        check = arr[x][y]
        # print(check)
        for i in range(x, x+n):
            for j in range(y, y+n):
                # print("arr[i][j] = ",arr[i][j])
                # print("check = ", check)
                if arr[i][j] != check:
                    recu(x, y, n//2)
                    recu(x, y+n//2, n//2)
                    recu(x+n//2, y, n//2)
                    recu(x+n//2, y+n//2, n//2)
                    return
        answer.append(check)
    recu(0, 0, len(arr))
    # print(answer)
    return [answer.count(0), answer.count(1)]
