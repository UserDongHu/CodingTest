def solution(s):
    answer = 0
    first = ':'
    count_first = 0
    count_not_first = 0
    for i in range(len(s)):
        if first == ':':
            first = s[i]
        if s[i] == first:
            count_first += 1
        else:
            count_not_first += 1
        if count_first == count_not_first:
            answer += 1
            count_first = 0
            count_not_first = 0
            first = ':'
    if count_first != count_not_first:
        answer += 1
    return answer