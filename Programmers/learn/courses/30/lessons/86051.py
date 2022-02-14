def solution(numbers):
    answer = 0
    for num in numbers:
        answer += num
    answer = 45 - answer
    return answer


print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
