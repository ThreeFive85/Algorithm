# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42890
# 참고 블로그 : https://codlingual.tistory.com/161

from itertools import combinations


def solution(relation):
    answer = 0
    n = len(relation[0])
    key_idx = list(range(n))
    candidate_keys = []

    for i in range(1, n+1):
        for comb in combinations(key_idx, i):
            # print("현재 comb : ", comb)
            hist = []
            for rel in relation:
                current_key = [rel[c] for c in comb]
                # print("현재 current_key : ", current_key)
                if current_key in hist:  # 중복검사
                    break
                else:
                    hist.append(current_key)
            else:
                for check in candidate_keys:  # 최소성 확인
                    if set(check).issubset(set(comb)):  # issubset은 부분집합인지 확인
                        break
                else:
                    candidate_keys.append(comb)
                    # print("candidate_keys에 들어가는 comb : ", comb)
    answer = len(candidate_keys)
    return answer


# ------------------------------------
# about .issubset()
# >>> {0, 1}.issubset({0, 1, 2})
# True
# >>> {1}.issubset({0, 1, 2})
# True
# >>> {1}.issubset({'A', 'B', 'C'})
# False
# >>> {1}.issubset(())
# False
# ------------------------------------


# solution([["100", "ryan", "music", "2"],
#           ["200", "apeach", "math", "2"],
#           ["300", "tube", "computer", "3"],
#           ["400", "con", "computer", "4"],
#           ["500", "muzi", "music", "3"],
#           ["600", "apeach", "music", "2"]])
