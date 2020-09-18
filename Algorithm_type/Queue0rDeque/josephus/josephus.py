# 문제 출처 : https://www.acmicpc.net/problem/11866

from sys import stdin

n, k = map(int, stdin.readline().split())
cal_list = []
for i in range(n):
    cal_list.append(i+1)

result = []
pop_num = 0
while len(cal_list) > 0:
    pop_num = (pop_num + (k - 1)) % len(cal_list)
    pop_element = cal_list.pop(pop_num)
    result.append(str(pop_element))

result = ", ".join(result)

print(f"<{result}>")
