def solution(N, stages):
    mystages = {}
    people = len(stages)
    for i in range(1, N+1):
        if stages.count(i) != 0:
            mystages[i] = stages.count(i)/people
            people -= stages.count(i)
        else:
            mystages[i] = 0
    return sorted([i for i in mystages], key=lambda x: mystages[x], reverse=True)