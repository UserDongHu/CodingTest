import re
def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s.sort(key=len)
    for i in s:
        i = list(map(int, i.split(',')))
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer
    
