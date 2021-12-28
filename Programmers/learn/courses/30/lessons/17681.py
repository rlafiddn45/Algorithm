def binary(n, number):
    arr = []
    while number > 0:
        arr.append(number % 2)
        number = number // 2
    while len(arr) < n:
        arr.append(0)
    return arr[::-1]


def solution(n, arr1, arr2):
    answer = [[' '] * n for _ in range(n)]
    for i in range(n):
        arr1[i] = binary(n, arr1[i])
        arr2[i] = binary(n, arr2[i])
    for i in range(n):
        for j in range(n):
            if arr1[i][j] + arr2[i][j] != 0:
                answer[i][j] = '#'
    for i in range(n):
        answer[i] = ''.join(answer[i])
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10])
