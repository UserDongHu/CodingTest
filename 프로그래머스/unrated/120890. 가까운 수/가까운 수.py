def solution(array, n):
    array.sort()
    min_index = min(range(len(array)), key=lambda i: abs(array[i] - n))
    return array[min_index]