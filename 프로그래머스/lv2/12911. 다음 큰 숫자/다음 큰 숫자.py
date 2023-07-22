def solution(n):
    def count(n):
        count = 0
        b = format(n, 'b')
        for i in b:
            if i == '1':
                count += 1
        return count
    answer = 0
    a = n
    while answer == 0:
        a += 1
        if count(n) == count(a):
            answer = a
    return answer