def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        first = arr1[i]
        second = arr2[i]
        wall = ''
        for j in bin(first | second)[2:].zfill(n):
            if(j == "1"):
                wall += '#'
            else:
                wall += ' '
        answer.append(wall)
    return answer