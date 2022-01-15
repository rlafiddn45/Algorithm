def check(s, graph):
    cnt = 0
    stack = [s]
    visit = [0] * len(graph)
    while stack:
        n = stack.pop()
        if visit[n] == 0:
            visit[n] = 1
            cnt += 1
        for i in range(len(graph)):
            if visit[i] == 0 and graph[n][i] == 1:
                stack.append(i)
    return cnt


def solution(n,  wires):
    answer = n
    graph = [[0] * n for _ in range(n)]
    for wire in wires:
        x, y = wire[0] - 1, wire[1] - 1
        graph[x][y] = graph[y][x] = 1
    for i in range(n):
        for j in range(i):
            if graph[i][j] == 1:
                graph[i][j], graph[j][i] = 0, 0
                cnt_i = check(i, graph)
                cnt_j = check(j, graph)
                answer = min(answer, abs(cnt_j - cnt_i))
                graph[i][j], graph[j][i] = 1, 1
    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
