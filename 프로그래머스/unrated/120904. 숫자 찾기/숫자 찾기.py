def solution(num, k):
    for i, j in enumerate(str(num)):
        if str(k) == j:
            return i + 1
    return -1