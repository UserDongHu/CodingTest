def solution(brown, yellow):
    for i in range(3, 2499): #가로
        for j in range(3, i+1): #세로
            if ((i*2) + ((j-2)*2) == brown) and ((i-2) * (j-2) == yellow):
                answer = [i, j]
                break
    return answer