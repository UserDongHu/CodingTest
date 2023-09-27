def solution(emergency):
    mye = sorted(emergency, reverse = True)
    answer = [mye.index(i)+1 for i in emergency]
    return answer