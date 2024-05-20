def solution(a, d, included):
    return sum([i[1] for i in zip(included, [a+d*i for i in range(len(included))]) if i[0]])