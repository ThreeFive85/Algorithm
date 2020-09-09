# 문제 출처 : https://www.acmicpc.net/problem/11508

'''
from sys import stdin // 입력값을 줄바꿈으로 받을 때 사용
n = int(input())
p = list(map(int, stdin.read().split()))
p = sorted(p)

result = 0
last_idx = p[-1]
slice_p = p[:-1]
slice_p.insert(0,last_idx)

start_idx = 0
end_idx = len(slice_p)

div = 3

for _ in range(start_idx, end_idx, div):
  arr = slice_p[start_idx:start_idx + div]
  arr.sort()
  if len(arr) < 3:
    result += sum(arr)
  else:
    result += (arr[1] + arr[2])
  start_idx = start_idx + div

print(result)

위 코드처럼 3개씩 묶어 묶음안에 제일 작은 수를 빼고 다 더하면 되겠다고 생각해서 작성했는데 예제 코드는 맞는데 테스트 케이스에서 틀린거 같다.
생각해보니 그냥 내림차순으로 정렬하여 인덱스에 3을 나눈 나머지 값이 2인 것들만 포함시키지 않므면 된다.
'''

from sys import stdin
n = int(input())
p = list(map(int, stdin.read().split()))
result = 0
p.sort(reverse=True)
for i in range(n):
    if i % 3 != 2:
        result += p[i]

print(result)
