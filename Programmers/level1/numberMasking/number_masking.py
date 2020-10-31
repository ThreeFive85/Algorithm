# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = ''
    for num in phone_number[:-4]:
        num = "*"
        answer += num
    answer += phone_number[-4:]

    print(answer)
    return answer

# def solution(phone_number):
#     return "*"*(len(phone_number)-4) + phone_number[-4:]
