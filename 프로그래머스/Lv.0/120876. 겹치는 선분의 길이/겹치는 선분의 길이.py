from collections import Counter
def solution(lines):
    answer = 0
    total = []
    for i in lines:
        for j in range(i[0], i[1]):
            total.append(j)
    mycounter = Counter(total)
    for j in mycounter:
        if mycounter[j] != 1:
            answer += 1
    return answer