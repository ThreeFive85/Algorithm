# 문제 출처 : https://www.acmicpc.net/problem/5430
# 참고 블로그 : https://jjangsungwon.tistory.com/3

from sys import stdin
from collections import deque

if __name__ == "__main__":
    test = int(stdin.readline())

    for i in range(test):
        p = input()
        n = int(stdin.readline())
        arr = input()
        arr = arr[1:-1]  # [] 제거
        if "," not in arr and arr != "":
            deque = deque([int(arr)])
        elif arr != "":
            deque = deque(map(int, arr.split(",")))
        else:
            deque = deque()

        flag = 1
        cnt = 0  # Reverse의 개수

        for i in range(len(p)):
            if p[i] == "R":
                cnt += 1
            else:
                if len(deque) == 0:
                    flag = 0
                    break

                if cnt % 2 == 0:
                    deque.popleft()
                else:
                    deque.pop()
        if cnt % 2 == 1:
            deque.reverse()

        if flag:
            print("[", end="")
            for i in range(len(deque)):
                if i == len(deque) - 1:
                    print(deque[i], end="")
                else:
                    print(str(deque[i]) + ",", end="")
            print("]")
        else:
            print("error")

# 어디서 런타임 에러가 나는 걸까...
