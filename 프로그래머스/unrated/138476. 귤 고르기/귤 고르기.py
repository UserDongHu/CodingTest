def solution(k, tangerine):
    answer = 0
    a = {}
    for i in tangerine:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
    b = sorted(a.values(), reverse=True)
    for j in b:
        if k <= 0:
            break
        k -= j
        answer += 1
    return answer