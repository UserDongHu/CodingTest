def solution(sides):
    a = max(sides)
    sides.remove(a)
    return 1 if a < sum(sides) else 2