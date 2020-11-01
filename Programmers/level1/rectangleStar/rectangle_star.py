# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/12969

# a, b = map(int, input().strip().split(' '))
# a_star = "".join(["*" for i in range(a)])
# for _ in range(b):
#     print(a_star)

a, b = map(int, input().strip().split(' '))
print(("*" * a + "\n") * b)
