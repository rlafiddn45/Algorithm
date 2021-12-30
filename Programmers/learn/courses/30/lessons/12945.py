def solution(n):
    n1, n2 = 0, 1
    while n > 0:
        n1, n2 = n2, n1 + n2
        n -= 1
    return n1 % 1234567


print(solution(3))
print(solution(8))
