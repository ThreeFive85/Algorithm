# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/67256
# 참고 블로그 : https://medium.com/@haeseok/프로그래머스-키패드-누르기-문제풀이-b4f24077bcfb

def distance(hand, number):
    location = {"1": (0, 0), "2": (0, 1), "3": (0, 2),
                "4": (1, 0), "5": (1, 1), "6": (1, 2),
                "7": (2, 0), "8": (2, 1), "9": (2, 2),
                "*": (3, 0), "0": (3, 1), "#": (3, 2)
                }
    x_hand, y_hand = location[hand]
    x_number, y_number = location[number]

    return abs(x_hand - x_number) + abs(y_hand - y_number)


def solution(numbers, hand):
    answer = ''
    left, right = "*", "#"
    for num in numbers:
        if num in [1, 4, 7]:
            answer += "L"
            left = str(num)
            continue  # 프로그래머스 테스트에서는 continue를 안적으면 한 개의 테스트에서 실패를 한다.
        elif num in [3, 6, 9]:
            answer += "R"
            right = str(num)
            continue  # ''
        elif num in [2, 5, 8, 0]:
            dis1 = distance(left, str(num))
            dis2 = distance(right, str(num))
            if dis1 < dis2:
                answer += "L"
                left = str(num)
            elif dis1 == dis2:
                if hand == "right":
                    answer += "R"
                    right = str(num)
                else:
                    answer += "L"
                    left = str(num)
            else:
                answer += "R"
                right = str(num)
    print(answer)
    return answer


solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")  # "LRLLLRLLRRL"
solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")  # "LRLLRRLLLRR"
solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right")  # "LLRLLRLLRL"
solution([0, 0, 0, 0, 0], "right")  # "RRRRR"
solution([0, 1, 2, 3, 4, 5], "left")  # "LLLRLL"
