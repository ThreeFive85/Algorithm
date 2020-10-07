# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    p_cnt = s.lower().count("p")
    y_cnt = s.lower().count("y")
    if p_cnt == y_cnt:
        return True
    else:
        return False

# def solution(s):
#     print(s.lower().count("p") == s.lower().count("y"))
#     return s.lower().count("p") == s.lower().count("y")


# solution('poooyY')
