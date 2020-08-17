def printer(priorities, location):
    count = 0
    m = max(priorities)

    while True:
        first = priorities.pop(0)
        if first == m:
            count += 1
            if location == 0:
                break
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(first)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1

    print(count)
    return count


# printer([2, 1, 3, 2], 2)
# printer([1, 1, 9, 1, 1, 1], 0)
