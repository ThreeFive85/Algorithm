# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/72410

import re
from collections import deque


def solution(new_id):
    answer = ''
    new_id1 = new_id.lower()
    new_id2 = re.sub('[^0-9a-z-_.]', '', new_id1)
    deq = deque(new_id2)
    new_id3 = ''
    while len(deq) > 0:
        pop = deq.popleft()
        if pop == '.':
            if not '.' in new_id3:
                new_id3 += pop
            if new_id3[-1] == '.':
                continue
            else:
                new_id3 += pop
        else:
            new_id3 += pop
    new_id4 = ''
    if new_id3[0] == '.':
        new_id4 += new_id3[1:]
    elif new_id3[-1] == '.':
        new_id4 += new_id3[:-1]
    else:
        new_id4 += new_id3
    new_id5 = ''
    if new_id4 == '':
        new_id5 += 'a'
    else:
        new_id5 += new_id4
    new_id6 = ''
    if len(new_id5) > 15:
        new_id6 = new_id5[:15]
    else:
        new_id6 = new_id5
    if new_id6[-1] == '.':
        new_id6 = new_id6[:-1]
    new_id7 = ''
    if len(new_id6) < 3:
        last = new_id6[-1]
        new_id7 += new_id6
        while len(new_id7) < 3:
            new_id7 += last
    else:
        new_id7 += new_id6
    # print(new_id7)
    return new_id7
