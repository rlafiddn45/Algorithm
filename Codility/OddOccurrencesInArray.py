def solution(A):
    values = {}
    for a in A:
        if a not in values:
            values[a] = 1
        else:
            values[a] = values[a] + 1
    for v, k in values.items():
        if k % 2:
            return v


# print(solution([9, 3, 9, 3, 9, 7, 9, 7, 9]))
# print(solution([9]))
print(solution([9, 9, 9, 9, 8]))