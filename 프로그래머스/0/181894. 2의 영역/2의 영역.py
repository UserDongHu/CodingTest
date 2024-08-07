def solution(arr):
    start = -1
    end = -1
    for i, j in enumerate(arr):
        if j==2:
            start = i
            break
    for i, j in enumerate(reversed(arr)):
        if j==2:
            end = -i-1
            break
    if start == -1 and end == -1:
        return [-1]
    return arr[start:end+1] if end != -1 else arr[start:]