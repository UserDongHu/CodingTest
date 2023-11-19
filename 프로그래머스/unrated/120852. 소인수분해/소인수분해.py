def solution(n):
    answer = set()
    a = 2
    while n != 1:
        if n % a == 0:
            n /= a
            answer.add(a)
            a = 2
        else:
            a += 1
    return sorted(list(answer))