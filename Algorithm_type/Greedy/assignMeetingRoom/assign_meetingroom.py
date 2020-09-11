# 문제 출처 : https://www.acmicpc.net/problem/1931

'''
해결 아이디어
    주어진 시작시간과 끝시간들을 이용해서 가장 많은 회의 수를 찾을려면 빨리 끝나는 회의 순서대로 정렬하여야 한다.
    그래야 빨리 끝날수록 다음 회의를 할 수 있기때문이다. 그래서 끝나는 시간으로 오름차순으로 정렬이 필요하다.
    또 고려해야 할 점은 끝나는 시간이 같다면 최대한 빨리 시작하는 순서로 정렬을 해야 한다.
    만약 (1 2), (2 2)가 있을 경우 (1 2)는 (2 2)의 끝나는 시간보다 시작시간이 일찍이기 때문에 무시되어
    1번으로 나오지만 시작시간 오름차순 정렬을 통한다면 1에서 2의 회의가 끝나고 2에서 2의 회의가 시작되기
    때문에 2번으로 잡을 수 있다.
    그래서 필요한 것은 먼저 끝나는 시간의 오름차순과 시작하는 시간의 오름차순 정렬이 필요하다.
    sort(key=lambda)를 사용하면 key에 튜플 형식으로 여러 인자를 주면 해당 인자의 순서대로 정렬을 해준다.
'''

import sys

n = int(sys.stdin.readline())
time = [[0]*2 for _ in range(n)]
for i in range(n):
    s, e = map(int, sys.stdin.readline().split())
    time[i][0] = s
    time[i][1] = e

time.sort(key=lambda x: (x[1], x[0]))

end_time = time[0][1]
count = 1

for i in range(1, n):
    if time[i][0] >= end_time:
        count += 1
        end_time = time[i][1]

print(count)
