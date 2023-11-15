import re

def solution(my_string):
    return sum(map(lambda x: int(x), re.findall('[0-9]', my_string)))