def solution(n):
    for i in range(1, n//2):
        if i**2 == n:
            return 1
    else:
        return 2