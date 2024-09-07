def solution(picture, k):
    answer = []
    for i in picture:
        for j in range(k):
            a = ''
            for l in i:
                a += l*k
            answer.append(a)
            
    return answer