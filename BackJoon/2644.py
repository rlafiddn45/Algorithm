from collections import deque

n = int(input())
s, e = map(int, input().split())
m = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    p, q = map(int, input().split())
    arr[p][q] = arr[q][p] = 1


def bfs(s_v):
    global e
    visit = [0] * (n + 1)
    queue = deque()
    queue.append(s_v)
    while queue:
        v = queue.popleft()
        if v == e:
            return visit[v]
        for w in range(n + 1):
            if visit[w] == 0 and arr[v][w] == 1:
                queue.append(w)
                visit[w] = visit[v] + 1
    return -1


print(bfs(s))

