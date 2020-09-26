# 문제 출처 : https://www.acmicpc.net/problem/1541
# 참고 블로그 : https://suri78.tistory.com/30


from sys import stdin
# string = '55-50+40'

string = stdin.readline().split('-')
# print(string)
part_sum = []
for t in string:
    temp = list(map(int, t.split('+')))
    # print(temp)
    part_sum.append(sum(temp))
# print(part_sum)
total = part_sum[0]
# print(part_sum[1:])
for p_sum in part_sum[1:]:
    total -= p_sum
print(total)
