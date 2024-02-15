def solution(answers):
    answer = []
    score = [0, 0, 0]
    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    for i in range(len(answers)):
        if answers[i] == a[i]:
            score[0] += 1
        if answers[i] == b[i]:
            score[1] += 1
        if answers[i] == c[i]:
            score[2] += 1
    if score[0] == max(score):
        answer.append(1)
    if score[1] == max(score):
        answer.append(2)
    if score[2] == max(score):
        answer.append(3)
    return answer