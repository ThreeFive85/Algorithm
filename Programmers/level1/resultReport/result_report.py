# https://programmers.co.kr/learn/courses/30/lessons/92334

# 문제 설명
# 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.

# 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.

# 다음은 전체 유저 목록이 ["muzi", "frodo", "apeach", "neo"]이고, k = 2(즉, 2번 이상 신고당하면 이용 정지)인 경우의 예시입니다.

# 유저 ID	유저가 신고한 ID     설명
# "muzi"	"frodo"	        "muzi"가 "frodo"를 신고했습니다.
# "apeach"	"frodo"	        "apeach"가 "frodo"를 신고했습니다.
# "frodo"	"neo"	        "frodo"가 "neo"를 신고했습니다.
# "muzi"	"neo"	        "muzi"가 "neo"를 신고했습니다.
# "apeach"	"muzi"	        "apeach"가 "muzi"를 신고했습니다.

# 각 유저별로 신고당한 횟수는 다음과 같습니다.

# 유저 ID	신고당한 횟수
# "muzi"	1
# "frodo"	2
# "apeach"	0
# "neo" 	2

# 위 예시에서는 2번 이상 신고당한 "frodo"와 "neo"의 게시판 이용이 정지됩니다.
# 이때, 각 유저별로 신고한 아이디와 정지된 아이디를 정리하면 다음과 같습니다.

# 유저 ID	유저가 신고한 ID	    정지된 ID
# "muzi"	["frodo", "neo"]	["frodo", "neo"]
# "frodo"	["neo"]	["neo"]
# "apeach"	["muzi", "frodo"]	["frodo"]
# "neo"	    없음	              없음

# 따라서 "muzi"는 처리 결과 메일을 2회, "frodo"와 "apeach"는 각각 처리 결과 메일을 1회 받게 됩니다.

def solution(id_list, report, k):
    result = [0] * len(id_list)
    report = list(set(report))
    report_dict = {}
    id_report = [set() for i in range(len(id_list))]

    id_dict = {}
    for i in range(len(id_list)):
        id_dict[id_list[i]] = i
    # print(id_dict)

    for i in range(len(report)):
        tmp = report[i].split()
        u = tmp[0]
        t = tmp[1]
        if t not in report_dict:
            report_dict[t] = 1
        else:
            if t in id_report[id_dict[u]]:
                continue
            report_dict[t] += 1
        id_report[id_dict[u]].add(t)
    # print(report_dict)
    # print(id_report)

    for key, value in report_dict.items():
        if value >= k:
            for i in range(len(id_list)):
                if key in id_report[i]:
                    result[i] += 1
    # print(result)
    return result


# l = ["muzi", "frodo", "apeach", "neo"]
# r = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# c = 2
# solution(l, r, c)
