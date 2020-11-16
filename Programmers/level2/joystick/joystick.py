# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42860
# 참고 블로그 : https://codedrive.tistory.com/28

def solution(name):
    answer = 0
    name = list(name)
    base = ["A"] * len(name)
    idx = 0
    while(True):
        rightidx = 1
        leftidx = 1
        if name[idx] != "A":
            if ord(name[idx]) - ord("A") > 13:
                answer += 26 - (ord(name[idx]) - ord("A"))
            else:
                answer += ord(name[idx]) - ord("A")
            name[idx] = "A"
        if name == base:
            break
        else:
            for i in range(1, len(name)):
                if name[idx + i] == "A":
                    rightidx += 1
                else:
                    break
                if name[idx - i] == "A":
                    leftidx += 1
                else:
                    break
            if rightidx > leftidx:
                answer += leftidx
                idx -= leftidx
            else:
                answer += rightidx
                idx += rightidx

    print(answer)
    return answer
