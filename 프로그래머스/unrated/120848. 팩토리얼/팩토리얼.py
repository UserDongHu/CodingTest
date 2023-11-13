def solution(n):
    a = 1
    sum = 1
    while sum <= n:
        sum *= a
        a += 1
    return a-2