def solution(s):
    a = s.split()
    tmp1 = int(a[0])
    tmp2 = int(a[1])
    for i in a:
        if tmp1 > int(i):
            tmp1 = int(i)
        if tmp2 < int(i):
            tmp2 = int(i)
    answer = f'{tmp1} {tmp2}'
    return answer