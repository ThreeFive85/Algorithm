# https://programmers.co.kr/learn/courses/30/lessons/86491?language=python3

def solution(sizes):

    w = [max(size[0], size[1]) for size in sizes]
    h = [min(size[0], size[1]) for size in sizes]

    return max(w) * max(h)
