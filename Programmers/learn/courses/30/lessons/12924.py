def solution(n):
    answer = 1  # n = n
    for i in range(1, n // 2 + 1):
        temp, num = 0, i
        while temp < n:
            temp += num
            num += 1
        if temp == n:
            answer += 1
    return answer


print(solution(15))
