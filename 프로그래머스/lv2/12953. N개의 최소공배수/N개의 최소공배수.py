def solution(arr):
    answer = 0
    x = 1
    for i in arr:
        x *= i
    for j in range(1, x+1):
        count = 0
        for k in arr:
            if j % k == 0:
                count += 1
        if count == len(arr):
            answer = j
            break
    return answer