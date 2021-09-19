# https://programmers.co.kr/learn/courses/30/lessons/12901?language=python3

def solution(a, b):
    answer = ''
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for i in range(a-1):
        day += months[i]
    day += (b-1)
    day = day % 7
    answer = days[day]
    return answer
