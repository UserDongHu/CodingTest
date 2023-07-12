def solution(s):
    a = list(s)
    count = 0
    answer = ''
    for i in a:
        if(i != ' '):
            if(count % 2 == 0):
                answer += i.upper()
                count += 1
            else:
                answer += i.lower()
                count += 1
        else:
            answer += ' '
            count = 0
    return answer