def solution(clothes):
    dif = {}
    answer = 1
    for i in clothes:
        if i[1] not in dif:
            dif[i[1]] = 1
        else:
            dif[i[1]] += 1
    print(dif)
    for j in dif:
        answer *= dif[j]+1
    return answer-1