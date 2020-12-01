# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    set_nums = set(nums)
    length = len(nums) // 2
    if length < len(set_nums) or length == len(set_nums):
        return length
    else:
        return len(set_nums)
