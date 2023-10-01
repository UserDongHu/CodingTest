def solution(progresses, speeds):
    answer = []
    result = 0
    while progresses:
        for _ in range(len(progresses)):
            if progresses[0] >= 100:
                progresses.pop(0)
                speeds.pop(0)
                result += 1
            else:
                break
        if result > 0:
            answer.append(result)
            result = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
    return answer