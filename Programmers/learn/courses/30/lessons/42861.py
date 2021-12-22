# 크루스칼 알고리즘 공부한 뒤 다시 도전한다

def solution(n, costs):
    answer, visit = 0, [0] * n
    bridges = [cost[2] for cost in costs]
    maximum = max(bridges)
    for i in range(n):
        if visit[i] == 0:
            idx, temp = 0, maximum
            for cost in costs:
                x, y, z = cost
                if z <= temp:
                    if i == x:
                        idx, temp = y, z
                    elif i == y:
                        idx, temp = x, z
            visit[i] = visit[idx] = 1
            answer += temp
    return answer


# print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
# print(solution(3, [[0, 1, 2], [0, 2, 1], [1, 2, 3]]))
# print(solution(4, [[0, 1, 1], [0, 2, 2], [0, 3, 7], [1, 3, 3], [1, 2, 5], [2, 3, 4]]))
print(solution(4, [[1, 3, 1], [0, 2, 3], [0, 3, 2]]))
