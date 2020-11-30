# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12913#
# 참고 블로그 : https://eda-ai-lab.tistory.com/480

def solution(land):
    for i in range(len(land)-1):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][1], land[i][0], land[i][3])
        land[i+1][3] += max(land[i][1], land[i][2], land[i][0])
    # print(land)
    return max(land[-1])
