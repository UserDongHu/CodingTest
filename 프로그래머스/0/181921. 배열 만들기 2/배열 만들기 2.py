def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if int(str(i).replace('5', '0')) == 0:
            answer.append(i)
    return answer if answer else [-1]