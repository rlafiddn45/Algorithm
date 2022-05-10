def solution(A, K):
    if len(A) == 0:
        return []
    return A[len(A) - K % len(A):] + A[:len(A) - K % len(A)]


print(solution([1, 1, 2, 3, 5], 42))
print(solution([], 2))
print(solution([1], 0))