from collections import deque


def bfs(s1, s2, d1, d2, arr):
    queue = deque([(s1, s2)])
    visit = [[0] * len(arr) for _ in range(len(arr))]
    visit[s1][s2] = 1
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    while queue:
        g, h = queue.popleft()
        if g == d1 and h == d2:
            return visit[g][h] - 1
        for i in range(8):
            if 0 <= g + dx[i] < len(arr) and 0 <= h + dy[i] < len(arr):
                if visit[g + dx[i]][h + dy[i]] == 0 or visit[g + dx[i]][h + dy[i]] > visit[g][h] + 1:
                    visit[g + dx[i]][h + dy[i]] = visit[g][h] + 1
                    queue.append((g + dx[i], h + dy[i]))
    return visit[d1][d2] - 1


T = int(input())
for t in range(T):
    n = int(input())
    chess = [[0] * n for _ in range(n)]
    x, y = map(int, input().split())
    p, q = map(int, input().split())
    cnt = bfs(x, y, p, q, chess)
    print(cnt)

