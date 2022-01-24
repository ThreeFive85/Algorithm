# https://programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product


def solution(word):

    list_word = ['A', 'E', 'I', 'O', 'U']
    for i in range(2, 6):
        list_word += [''.join(word)
                      for word in list(product('AEIOU', repeat=i))]
    list_word.sort()
    return list_word.index(word)+1
