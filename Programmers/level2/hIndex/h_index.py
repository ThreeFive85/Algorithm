# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42747
# 참고 블로그 : https://ychae-leah.tistory.com/96

def solution(citations):
    citations.sort(reverse=True)
    answer = max(list(map(min, enumerate(citations, start=1))))
    return answer
