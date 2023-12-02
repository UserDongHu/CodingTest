def solution(s):
    result = 0
    array = s.split(" ")
    pre = 0
    for i in array:
        if i == 'Z':
            result -= pre
        else:
            pre = int(i)
            result += int(i)
    return result