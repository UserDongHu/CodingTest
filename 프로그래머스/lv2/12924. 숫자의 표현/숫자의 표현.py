def solution(n):
    answer = 0
    for a in range(1, 10000):
        for d in range(1, 10000):
            sum = (d * (a + a + d - 1)) / 2
            if sum == n :
                answer += 1
            if sum > n :
                break
    return answer