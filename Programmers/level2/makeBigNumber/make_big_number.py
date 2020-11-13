# 문제 출처 : https://programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = number[:-k]
    # print(stack)
    return "".join(stack)


'''
제거 된 숫자
stack = []
for i in range(0, len(number), k):
    slice_k = list(number[i:i+k])
    # print(slice_k)
    for num in slice_k:
        if num != max(slice_k):
            if len(stack) == k:
                break
            else:
                stack.append(num)
'''
