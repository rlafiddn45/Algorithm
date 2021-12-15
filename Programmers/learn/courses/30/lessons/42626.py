import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        m, n = heapq.heappop(scoville), heapq.heappop(scoville)
        mixed = m + n * 2
        heapq.heappush(scoville, mixed)
        answer += 1
    return answer

