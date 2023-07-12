def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        sizes[i].sort()
    print(sizes)
    w, h = 0, 0
    for j in range(len(sizes)):
        if w < sizes[j][0]:
            w = sizes[j][0]
        if h < sizes[j][1]:
            h = sizes[j][1]
    answer = w * h
    return answer