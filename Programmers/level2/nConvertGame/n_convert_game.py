# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/17687
# 참고 블로그 : https://kdgt-programmer.tistory.com/12

def solution(n, t, m, p):
    answer = ''
    for i in range(0, t*m):
        answer += convert(i, n)
    # print(answer)
    # print(list(answer))
    return ''.join(list(answer)[m*j+p-1] for j in range(t))

# 진법 변환 함수


def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
