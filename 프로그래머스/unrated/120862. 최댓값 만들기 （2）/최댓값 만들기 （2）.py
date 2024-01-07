def solution(numbers):
    numbers.sort()
    yang = numbers[0] * numbers[1]
    numbers.sort(reverse=True)
    eum = numbers[0] * numbers[1]
    return yang if yang > eum else eum