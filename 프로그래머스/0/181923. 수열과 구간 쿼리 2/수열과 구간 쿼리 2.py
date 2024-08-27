def solution(arr, queries):
    answer = []
    for i in queries:
        myresult = sorted(filter(lambda x: x>i[2], arr[i[0]:i[1]+1]))
        answer.append(myresult[0]) if myresult else answer.append(-1)
    return answer