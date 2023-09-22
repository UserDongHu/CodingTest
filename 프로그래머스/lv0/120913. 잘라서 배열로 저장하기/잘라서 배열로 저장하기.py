import re

def solution(my_str, n):
    p = re.compile(rf'.{{1,{n}}}')
    answer = p.findall(my_str)
    return answer