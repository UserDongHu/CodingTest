def solution(arr):
    answer = 0
    while True:
        if arr == calc(arr):
            break
        answer += 1
        arr = calc(arr)
    return answer

def calc(arr):
    newarr = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            newarr.append(int(i/2))
        elif i < 50 and i % 2 == 1:
            newarr.append(i*2+1)
        else:
            newarr.append(i)
    return newarr