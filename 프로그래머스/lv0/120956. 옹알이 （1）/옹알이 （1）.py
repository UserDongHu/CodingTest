import re
def solution(babbling):
    answer = 0
    for i in babbling:
        if re.sub('aya|ye|woo|ma', '', i) == '':
            answer += 1
    return answer