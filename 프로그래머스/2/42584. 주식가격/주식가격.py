def solution(prices):
    answer = []
    for i, j in enumerate(prices):
        sec = 0
        index = i
        while index != len(prices)-1:
            if j <= prices[index]:
                sec += 1
                index += 1
            else:
                break
        answer.append(sec)
    return answer