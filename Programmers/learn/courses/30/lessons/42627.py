import heapq


def solution(jobs):
    answer = 0
    heap, processing, using, end = [], [], 0, 0
    for job in jobs:
        heapq.heappush(heap, job)
    while heap:
        print(processing, using, end)
        # 사용중을 판단
        # 첫번째 작업의 시작 시간이 현재 시간보다 작다면 -> 하드디스크 사용중
        temp = using
        if heap[0][0] < answer:
            using = 1
        else:
            using = 0
        # 사용 여부가 변경된다면 heap 의 변경이 필요
        if temp != using:
            heap = change(heap)
        if using == 0:  # 하드 디스크가 사용중이 아닌 경우 -> [요청 시간, 수행 시간]
            processing = heapq.heappop(heap)
            # 작업시간 + 이전 작업이 끝난 후의 대기시간
            # answer += processing[1] - processing[0] + processing[0] - end
            answer += 
            end += processing[1]
        else:  # 하드 디스크가 사용중인 경우 -> [수행 시간, 요청 시간]
            processing = heapq.heappop(heap)
            answer += end - processing[1] + processing[0]
            end += processing[0]
    print(answer)
    return answer // len(jobs)


def change(arr):
    heap = []
    for a in arr:
        heapq.heappush(heap, [a[1], a[0]])
    return heap


# print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[6, 2], [3, 1], [1, 2], [2, 4]]))

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
  3 3
    4 4 4 4 4
      2 2 2 2 2
            1 1 1 1