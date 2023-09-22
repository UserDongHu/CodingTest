import re

def solution(order):
    p = re.compile(r'[369]')
    answer = len(p.findall(str(order)))
    return answer