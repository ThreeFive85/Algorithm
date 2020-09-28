# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/60057
# 참고 블로그 : https://velog.io/@devjuun_s/문자열-압축-프로그래머스python2020-Kakao-공채

def solution(s):
    new_s = ''
    len_arr = []

    if len(s) == 1:
        return 1
    for cut in range(1, len(s)//2 + 1):
        # print(cut)
        count = 1
        temp_str = s[:cut]
        for i in range(cut, len(s), cut):
            if s[i:i+cut] == temp_str:
                count += 1
            else:
                if count == 1:
                    count = ''
                new_s += str(count) + temp_str
                temp_str = s[i:i+cut]
                count = 1
        if count == 1:
            count = ''
        new_s += str(count) + temp_str
        len_arr.append(len(new_s))
        new_s = ''

    print(min(len_arr))
    return min(len_arr)
