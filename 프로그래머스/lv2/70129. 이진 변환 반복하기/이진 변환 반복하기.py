def solution(s):
    answer = []
    count = 0
    sum = 0
    while s != '1': 
        x = ''
        count += 1
        for i in s:
            if i == '0':
                sum += 1
            elif i == '1':
                x += i
        s = format(len(x), 'b')
    answer.append(count)
    answer.append(sum)
    return answer