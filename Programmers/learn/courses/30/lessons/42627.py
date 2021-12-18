import heapq


def solution(jobs):
    answer, start, now, idx = 0, -1, 0, 0
    heap = []
    while idx < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, [job[1], job[0]])
        if heap:
            job = heapq.heappop(heap)
            start = now
            now += job[0]
            answer += now - job[1]
            idx += 1
        else:
            now += 1
    return answer // (len(jobs))


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[6, 2], [3, 1], [1, 2], [2, 4]]))
