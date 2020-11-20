# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42577

from collections import deque


def solution(phone_book):
    answer = True
    phone_book.sort()
    books = deque(phone_book)
    while len(books) > 0:
        con = books.popleft()
        for num in books:
            if con == num[:len(con)]:
                answer = False
                return answer
    return answer
