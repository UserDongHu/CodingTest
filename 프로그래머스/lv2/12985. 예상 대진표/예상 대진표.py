def change(c):
        if c % 2 == 1:
            return (c+1) / 2
        else:
            return c / 2
def solution(n,a,b):
    answer = 0
    while True:
        if a == b:
            break
        answer += 1
        a = change(a)
        b = change(b)
    return answer