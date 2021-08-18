# https://programmers.co.kr/learn/courses/30/lessons/83201#

def solution(scores):
    answer = []

    for i in range(len(scores)):
        tmp = []
        student_score = scores[i][i]  # 자신에게 준 점수
        for j in range(len(scores)):  # 학생의 총 점수를 tmp에
            tmp.append(scores[j][i])
        # print(tmp)
        # print(student_score)
        if max(tmp) == student_score and tmp.count(max(tmp)) == 1:
            tmp.remove(student_score)
        elif min(tmp) == student_score and tmp.count(min(tmp)) == 1:
            tmp.remove(student_score)
        avg = sum(tmp) / len(tmp)
        if avg >= 90:
            answer.append('A')
        elif avg >= 80:
            answer.append('B')
        elif avg >= 70:
            answer.append('C')
        elif avg >= 50:
            answer.append('D')
        else:
            answer.append('F')

    return ''.join(answer)
