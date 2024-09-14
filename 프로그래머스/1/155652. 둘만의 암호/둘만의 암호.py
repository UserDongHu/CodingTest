def solution(s, skip, index):
    answer = ''
    my_ap = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in skip:
        my_ap.remove(i)
    for i in s:
        answer += my_ap[(my_ap.index(i)+index)%len(my_ap)]
    return answer