def solution(emergency):
    rate = 1
    answer = emergency[:]
    while sum(emergency) != 0:
        myindex = emergency.index(max(emergency))
        answer[myindex] = rate
        rate += 1
        emergency[myindex] = 0
    return answer