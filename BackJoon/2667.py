N = int(input())
arr = [list(map(int, str(input()))) for _ in range(N)]
visit = [[0] * N for _ in range(N)]


def is_way(p, q):
    global N
    ret = True
    ret = True if 0 <= p < N and 0 <= q < N and arr[p][q] == 1 else False
    return ret


def dfs(s_x, s_y):
    global visit
    stack = [(s_x, s_y)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    cnt = 0
    while stack:
        x, y = stack.pop()
        if visit[x][y] == 0:
            visit[x][y] = 1
            cnt += 1
        for d in range(4):
            if is_way(x + dx[d], y + dy[d]) and visit[x + dx[d]][y + dy[d]] == 0:
                stack.append((x + dx[d], y + dy[d]))
    return cnt


apart = []
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0 and arr[i][j] == 1:
            apart.append(dfs(i, j))
print(len(apart))
apart.sort()
for a in apart:
    print(a)
