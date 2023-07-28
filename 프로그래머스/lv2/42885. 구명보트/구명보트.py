def solution(people, limit):
    count = 0
    head = 0
    back = 0
    people.sort()
    while head + back != len(people):
        count += 1
        if head + back + 1 == len(people):
            break
        else:
            if people[(back+1)*-1] + people[head] <= limit:
                head += 1
                back += 1
            else:
                back += 1
    return count