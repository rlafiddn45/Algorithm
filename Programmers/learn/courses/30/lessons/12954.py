def solution(x, n):
    return [x + i * x for i in range(n)]


print(solution(2, 5))
print(solution(4, 3))
print(solution(-4, 2))
