# https://programmers.co.kr/learn/courses/30/lessons/12978?language=python3
# 참고 블로그 : https://blog.naver.com/PostView.naver?blogId=ndb796&logNo=221234424646&redirect=Dlog&widgetTypeCall=true&directAccess=false

import heapq


def solution(N, road, K):

    INF = float('inf')
    vil = [INF] * (N+1)
    vil[1] = 0
    ad = [[] for _ in range(N+1)]
    for r in road:
        ad[r[0]].append([r[1], r[2]])
        ad[r[1]].append([r[0], r[2]])
    print(ad)
    dij(vil, ad)
    print("vil : ", vil)
    answer = [x for x in vil if x <= K]
    print("answer : ", answer)
    return len(answer)


def dij(vil, ad):
    heap = []
    heapq.heappush(heap, [0, 1])

    while heap:
        cost, node = heapq.heappop(heap)
        for n, c in ad[node]:
            print(f'{node} => n : {n}, c : {c}')
            if cost + c < vil[n]:
                vil[n] = cost + c
                heapq.heappush(heap, [cost+c, n])


# solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
#          [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
