# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = []
    while len(numbers) > 1:
        first = numbers.pop(0)
        for i in numbers:
            sum = first + i
            if sum not in answer:
                answer.append(sum)
    # print(sorted(answer))
    return sorted(answer)
