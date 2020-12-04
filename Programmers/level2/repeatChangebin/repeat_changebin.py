# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    cnt_o = s.count("0")
    cnt = 0
    while True:
        if s == "1":
            break
        else:
            s = change(s)
            cnt_o += s.count("0")
            cnt += 1
    print(cnt, cnt_o)
    return [cnt, cnt_o]


def change(s):
    x = ''
    for char in s:
        if char == '0':
            continue
        else:
            x += char
    print(format(len(x), "b"))
    return format(len(x), "b")


# about bin() : https://docs.python.org/ko/3/library/functions.html#bin
change("01110")
