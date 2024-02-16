def get_atk(number):
    attack = 0
    for i in range(1, int(number**(1/2))+1):
        if number%i == 0:
            if i**2 != number:
                attack += 2
            else:
                attack += 1
    return attack

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        if (atk := get_atk(i)) > limit:
            answer += power
        else:
            answer += atk
    return answer