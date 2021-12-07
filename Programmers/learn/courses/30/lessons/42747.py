def solution(citations):
    answer = 0
    h = 0
    while h <= max(citations):
        more, less = 0, 0
        for j in range(len(citations)):
            if citations[j] >= h:
                more += 1
            else:
                less += 1
        if less <= h <= more:
            answer = h
        h += 1
    return answer


print(solution([3, 0, 6, 1, 5]))
print(solution([1, 100, 3, 1, 3]))
print(solution([2]))


def solution1(citations):
    answer = 0
    citations.sort(reverse=True)
    for i, citation in enumerate(citations):
        if i > citation:
            return i
    return len(citations)


print(solution1([3, 0, 6, 1, 5]))
print(solution1([1, 100, 3, 1, 3]))

