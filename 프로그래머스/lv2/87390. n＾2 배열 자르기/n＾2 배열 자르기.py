def solution(n, left, right):
    answer = []
    for k in range(left, right+1):
        answer.append(k//n+1 if k//n+1 > k%n+1 else k%n+1)
    return answer