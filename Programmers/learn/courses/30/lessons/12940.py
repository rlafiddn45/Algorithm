def solution(n, m):
    num1, num2 = n, m
    while n % m != 0:
        n, m = m, n % m
    answer = [m, num1 * num2 // m]
    return answer


print(solution(3, 12))
