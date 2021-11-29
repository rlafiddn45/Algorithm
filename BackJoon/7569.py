from collections import deque

M, N, H = map(int, input().split())
arr = [[[] for _ in range(N)] for _ in range(H)]
for h in range(H):
    for n in range(N):
        arr[h][n].extend(list(map(int, input().split())))
visit = [[[0] * M for _ in range(N)] for _ in range(H)]


def is_way(x1, y1, z1):
    global M, N, H
    if x1 < 0 or x1 >= H:
        return False
    if y1 < 0 or y1 >= N:
        return False
    if z1 < 0 or z1 >= M:
        return False
    if arr[x1][y1][z1] != 0:
        return False
    return True


def bfs():
    global visit
    global queue
    dx = [0, -1, 0, 1, 0, 0]
    dy = [-1, 0, 1, 0, 0, 0]
    dz = [0, 0, 0, 0, -1, 1]
    day = 0
    while queue:
        x, y, z = queue.popleft()
        day = visit[x][y][z] if day < visit[x][y][z] else day
        for d in range(6):
            if is_way(x + dx[d], y + dy[d], z + dz[d]) and visit[x + dx[d]][y + dy[d]][z + dz[d]] == 0:
                queue.append((x + dx[d], y + dy[d], z + dz[d]))
                visit[x + dx[d]][y + dy[d]][z + dz[d]] = visit[x][y][z] + 1
    return day


end_day = 0
queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if visit[i][j][k] == 0 and arr[i][j][k] == 1:
                queue.append((i, j, k))
end_day = bfs()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if visit[i][j][k] == 0 and arr[i][j][k] == 0:
                end_day = -1

print(end_day)
