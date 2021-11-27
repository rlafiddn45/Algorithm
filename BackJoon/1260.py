from collections import deque

N, M, V = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1


# 너비 우선 탐색
def bfs(v):
    visit = [0] * (N + 1)
    queue = deque()
    queue.append(v)

    while queue:
        v = queue.popleft()
        visit[v] = 1
        print(v, end=" ")

        for w in range(len(graph[v])):
            if graph[v][w] == 1 and visit[w] == 0:
                visit[w] = 1
                queue.append(w)


# 깊이 우선 탐색
def dfs(v, visit):
    visit[v] = 1
    print(v, end=" ")

    for w in range(len(graph[v])):
        if graph[v][w] == 1 and visit[w] == 0:
            dfs(w, visit)


dfs(V, [0] * (N + 1))
print()
bfs(V)
