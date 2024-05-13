def solution(rank, attendance):
    a = sorted(filter(lambda x: x[1], zip(rank, attendance, [i for i in range(len(rank))])), key=lambda x: x[0])
    return a[0][2]*10000 + a[1][2]*100 + a[2][2]