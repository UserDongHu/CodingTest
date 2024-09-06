def solution(arr, query):
    a = 0
    for i in query:
        if a%2 == 0:
            arr = arr[:i+1]
        else:
            arr = arr[i:]
        a += 1
    return arr