def solution(n):
    answer = 0
    while n != 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n -= 1
            answer += 1
    return answer


print(solution(5))
print(solution(6))
print(solution(5000))
