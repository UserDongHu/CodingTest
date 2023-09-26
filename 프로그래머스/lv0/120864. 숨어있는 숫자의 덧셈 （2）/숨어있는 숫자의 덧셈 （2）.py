import re
def solution(my_string):
    mylist = re.findall(r'[0-9]+', my_string)
    return sum(map(int, mylist))