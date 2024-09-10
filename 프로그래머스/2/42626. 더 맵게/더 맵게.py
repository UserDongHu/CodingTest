import heapq as hp

def solution(scoville, K):
    answer = 0
    hp.heapify(scoville)
    while scoville[0] < K and len(scoville) >= 2:
        hp.heappush(scoville, hp.heappop(scoville) + hp.heappop(scoville)*2)
        answer += 1
    if scoville[0] >= K:
        return answer
    else:
        return -1