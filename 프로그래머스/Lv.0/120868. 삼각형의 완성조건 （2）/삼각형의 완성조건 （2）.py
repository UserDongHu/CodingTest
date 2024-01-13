def solution(sides):
    answer = 0
    for i in range(1, sum(sides)):
        mysides = sides[:]
        mysides.append(i)
        if max(mysides) < sum(mysides) - max(mysides):
            answer += 1
    return answer