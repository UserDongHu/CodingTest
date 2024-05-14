def solution(num_list):
    return sum(num_list) if len(num_list)>=11 else mul(num_list)

def mul(num_list):
    a = 1
    for i in num_list:
        a*=i
    return a