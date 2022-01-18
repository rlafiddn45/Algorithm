from collections import deque


def bfs(graph, v):
    queue = deque([v])
    visit = [0] * len(graph)
    while queue:
        n = queue.popleft()
        for i in range(1, len(graph)):
            if graph[n][i] != 0:
                if visit[i] == 0 or graph[n][i] + visit[n] < visit[i]:
                    queue.append(i)
                    visit[i] = graph[n][i] + visit[n]
    return visit


def solution(N, road, K):
    answer = 0
    graph = [[0] * N for _ in range(N)]
    for r in road:
        x, y, d = r[0] - 1, r[1] - 1, r[2]
        if graph[x][y] == graph[y][x] == 0:
            graph[x][y] = graph[y][x] = d
        else:
            temp = min(graph[x][y], d)
            graph[x][y] = graph[y][x] = temp
    visit = bfs(graph, 0)
    for v in visit:
        if v <= K:
            answer += 1
    return answer


# print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))
# print(solution(3, [[3, 2, 3], [3, 1, 1]], 3))

