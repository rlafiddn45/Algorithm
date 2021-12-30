def solution(arr1, arr2):  # arr1 = l * m, arr2 = m * n
    l, m, n = len(arr1), len(arr1[0]), len(arr2[0])
    answer = [[0] * n for _ in range(l)]  # l * n
    for i in range(l):
        for j in range(n):
            temp = 0
            for k in range(m):
                temp += arr1[i][k] * arr2[k][j]
            answer[i][j] = temp
    return answer


print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
