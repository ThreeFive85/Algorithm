import sys

strings = sys.stdin.readlines()
for string in strings[:-1]:
    brackets = []
    for i in string:
        print(i)
        if i in '([':
            brackets.append(i)
        elif i == ']':
            if not brackets or brackets.pop() != '[':
                print('no')
                break
        elif i == ')':
            if not brackets or brackets.pop() != '(':
                print('no')
                break
        elif i == '.':
            if brackets:
                print('no')
            else:
                print('yes')
