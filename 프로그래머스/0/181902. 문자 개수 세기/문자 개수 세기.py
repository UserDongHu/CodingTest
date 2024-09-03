from collections import Counter

def solution(my_string):
    answer = [0 for i in range(52)]
    for i in Counter(my_string):
        if ord(i) <= 90:
            answer[ord(i)-65] += Counter(my_string)[i]
        else:
            answer[ord(i)-71] += Counter(my_string)[i]
    return answer