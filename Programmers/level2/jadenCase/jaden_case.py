# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12951#
# 참고 블로그 : https://eda-ai-lab.tistory.com/490

# 공백도 그대로 표현되어야 한다.

def solution(s):
    answer = ''
    for idx, i in enumerate(s):
        if idx == 0:
            answer = i.upper()
        elif s[idx-1] == ' ':
            answer = ''.join([answer, i.upper()])
            # print('answer : ', answer)
        else:
            answer = ''.join([answer, i.lower()])
            # print(answer)
    return answer


'''
answer = ' '
s = 'world'
answer = ''.join([answer, s.upper()])
print(answer)
'''
