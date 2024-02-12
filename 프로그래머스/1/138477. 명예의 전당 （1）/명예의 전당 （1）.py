def solution(k, score):
    answer = []
    rank = []
    for i in score:
        rank.append(i)
        rank.sort()
        if len(rank) <= k:
            answer.append(rank[0])
        else:
            answer.append(rank[-k])
    return answer