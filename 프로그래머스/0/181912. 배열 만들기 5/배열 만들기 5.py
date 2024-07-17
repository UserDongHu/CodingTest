def solution(intStrs, k, s, l):
    return list(filter(lambda x: x>k, [int(i[s:s+l]) for i in intStrs]))