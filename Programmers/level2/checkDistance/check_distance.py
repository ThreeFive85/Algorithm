# https://programmers.co.kr/learn/courses/30/lessons/81302

# 3중 for문으로 P와 X를 찾음
# 각 대기실마다 5*5 int 배열을 만듬
# 현재 위치가 P이면 int 배열에 현재 위치와 현재 위치의 상하좌우 위치에 -1씩을 더해줌
# 현재 위치가 X면 int 배열에 현재 위치에 10을 더해주고 현재 위치에서 상하좌우에 만약 P가 있다면 칸막이가 존재하므로 안전하다는 뜻으로 3이상의 값을
# 더해줌
# 최종적으로 int 배열을 확인해서 -1보다 작은 값이 존재하면 거리두기를 하지 않은 것으로 판명하여 0을 리턴

from itertools import chain


def solution(places):
    answer = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for place in places:
        int_arr = [[0]*5 for _ in range(5)]
        for i in range(len(place)):
            for j in range(len(place[i])):
                if place[i][j] == 'P':
                    int_arr[i][j] += -1
                    for k in range(4):
                        nx = dx[k] + j
                        ny = dy[k] + i
                        if 0 <= ny < 5 and 0 <= nx < 5:
                            int_arr[ny][nx] += -1
                if place[i][j] == 'X':
                    int_arr[i][j] = 10
                    for k in range(4):
                        nx = dx[k] + j
                        ny = dy[k] + i
                        if 0 <= ny < 5 and 0 <= nx < 5 and int_arr[ny][nx] == 'P':
                            int_arr[ny][nx] += 3

        # print(int_arr)
        # print(list(chain(*int_arr)))
        if min(list(chain(*int_arr))) < -1:
            answer.append(0)
        else:
            answer.append(1)

    return answer
