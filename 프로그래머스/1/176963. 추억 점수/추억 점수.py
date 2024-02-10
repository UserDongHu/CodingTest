def solution(name, yearning, photo):
    answer = []
    for i in photo:
        sum_ = 0
        for j in i:
            if j in name:
                sum_ += yearning[name.index(j)]
        answer.append(sum_)
    return answer