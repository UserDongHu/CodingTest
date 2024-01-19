def solution(score):
    answer = []
    myscore = sorted(score, reverse=True, key=lambda x:x[0]+x[1])
    myrank = [1]
    rank = 1
    for i in range(1, len(myscore)):
        if myscore[i][0]+myscore[i][1] == myscore[i-1][0]+myscore[i-1][1]:
            myrank.append(rank)
        else:
            rank = i+1
            myrank.append(rank)
    for i in score:
        for j, k in zip(myrank, myscore):
            if i == k:
                answer.append(j)
    return answer