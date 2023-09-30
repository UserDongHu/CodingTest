def solution(n):
    return len(list(filter(lambda x: n%x==0, range(1, n+1))))