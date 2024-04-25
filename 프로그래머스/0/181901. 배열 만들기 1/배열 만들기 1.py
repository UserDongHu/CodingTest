def solution(n, k):
    answer = []
    a = k
    while a <= n:
        answer.append(a)
        a += k
    return answer