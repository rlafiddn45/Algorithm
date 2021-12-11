# def solution(numbers, target):
#     answer = 0
#     results = [0]
#     for number in numbers:
#         temp = []
#         for result in results:
#             temp.append(result + number)
#             temp.append(result - number)
#         results = temp
#     for result in results:
#         if result == target:
#             answer += 1
#     return answer


def solution(numbers, target):
    answer = 0
    results = [[]]
    for number in numbers:
        temp = []
        for result in results:
            temp.append(result + [number])
            temp.append(result + [-number])
        results = temp
    for result in results:
        if sum(result) == target:
            answer += 1
    return answer


print(solution([1, 1, 1, 1, 1], 3))
