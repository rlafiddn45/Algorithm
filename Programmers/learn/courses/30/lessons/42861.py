def solution(n, costs):
    answer = 0
    costs.sort()
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        temp, idx = 10000, 0
        for cost in costs:
            x, y, val = cost
            if i == x:
                if temp > val:
                    temp = val
                    idx = y
            elif i == y:
                if temp > val:
                    temp = val
                    idx = x
        if visit[i][idx] == visit[idx][i] == 0:
            visit[i][idx] = visit[idx][i] = 1
            answer += temp
    return answer


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
