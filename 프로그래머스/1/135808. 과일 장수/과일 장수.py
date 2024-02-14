def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    box = m
    while m <= len(score):
        answer += score[m-1]*box
        m += box
    return answer