def solution(code):
    answer = ''
    mode = 0
    for i, j in enumerate(code):
        if mode == 0:
            if j == '1':
                mode = 1
            else:
                if i % 2 == 0:
                    answer += j
        else:
            if j == '1':
                mode = 0
            else:
                if i % 2 == 1:
                    answer += j
    return answer if answer != '' else 'EMPTY'