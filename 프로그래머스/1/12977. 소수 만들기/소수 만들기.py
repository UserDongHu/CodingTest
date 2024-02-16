from itertools import combinations

def is_so(nums):
    for i in range(2, nums):
        if nums%i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    for i in list(combinations(nums, 3)):
        if is_so(sum(i)):
            answer += 1
    return answer