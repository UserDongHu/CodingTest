def solution(n):
    answer = 0
    a = [0, 1]
    for i in range(3, n+2):
        a.append(a[i-3] + a[i-2])
    answer = a[n] % 1234567
    return answer