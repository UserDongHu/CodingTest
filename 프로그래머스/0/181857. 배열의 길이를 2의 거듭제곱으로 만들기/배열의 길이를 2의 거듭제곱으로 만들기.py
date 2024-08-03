def solution(arr):
    a = 0
    while len(arr) > 2**a:
        a += 1
    for i in range(2**a - len(arr)):
        arr.append(0)
    return arr
            