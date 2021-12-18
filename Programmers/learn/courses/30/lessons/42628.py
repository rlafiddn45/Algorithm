import heapq


def solution(operations):
    heap = []
    for operation in operations:
        cmd, val = operation.split()
        if cmd == 'I':
            heapq.heappush(heap, int(val))
        elif cmd == 'D':
            if heap:
                if len(val) == 1:
                    heap.sort()
                    heap.pop()
                    heapq.heapify(heap)
                else:
                    heapq.heappop(heap)
    if not heap:
        return [0, 0]
    else:
        heap.sort()
        return [heap[-1], heap[0]]


# print(solution(["I -1", "I 15", "I 16", "I 3", "I -34"]))
print(solution(["I -1", "I 15", "I 16", "I 3", "D 1", "I -34"]))
# print(solution(["I 16", "D 1"]))
# print(solution(["I 7","I 5","I -5","D -1"]))
# print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
# print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
