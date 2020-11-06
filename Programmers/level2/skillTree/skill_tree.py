# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/49993?language=python3

def solution(skill, skill_trees):
    answer = 0
    filter_skill = []
    for i in range(len(skill_trees)):
        filter_char = ''
        for char in skill_trees[i]:
            if char in skill:
                filter_char += char
        filter_skill.append(filter_char)
    print(filter_skill)
    for skill_char in filter_skill:
        if skill_char == skill[0:len(skill_char)]:
            answer += 1
    print(answer)
    return answer
