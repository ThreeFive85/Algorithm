# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/17686
# 참고 블로그 : https://codingspooning.tistory.com/23

import re


def solution(files):
    answer = []
    split = []
    for file in files:
        split.append(re.split(r"([0-9]+)", file))
    print(split)
    sort_sp = sorted(split, key=lambda x: (x[0].lower(), int(x[1])))
    print(sort_sp)
    for sp in sort_sp:
        answer.append(''.join(sp))
    return answer


'''
실패한 코드

tu = []
    for file in files:
        if file[1] == '-':
            tu.append((file, file[0]))
        else:
            p = re.findall('\d+', file)[0]
            tu.append((file,int(p)))
    tup = sorted(tu, key=lambda x: (x[0][0].lower(), x[1]))
    print(tup)
    for tu in tup:
        answer.append(tu[0])
4개의 테스트를 통과하지 못함
'''
