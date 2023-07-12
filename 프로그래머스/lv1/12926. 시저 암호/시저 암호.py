def solution(s, n):
    answer = ''
    a = list(s)
    for i in a:
        for j in range(n):
            if i not in (' ', 'z', 'Z'):
                i = chr(ord(i)+1)
            elif i in ('z', 'Z'):
                i = chr(ord(i)-25)
            else:
                break
        answer += i
    return answer