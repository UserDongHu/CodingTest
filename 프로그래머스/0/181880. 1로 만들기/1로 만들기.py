def solution(num_list):
    answer = 0
    for i in num_list:
        while i != 1:
            i = calc(i)
            answer += 1
    return answer

def calc(num):
    if num%2 == 0:
        return num/2
    else:
        return (num-1)/2