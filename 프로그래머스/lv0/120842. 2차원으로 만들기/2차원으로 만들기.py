def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        myarray = []
        for j in range(i, i + n):
            myarray.append(num_list[j])
        answer.append(myarray)
    return answer