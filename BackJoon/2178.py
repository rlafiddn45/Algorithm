from collections import deque
#
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# N, M = map(int, input().split())
# arr = [[] for _ in range(N)]
# for i in range(N):
#     arr[i].extend(map(int, list(str(input()))))
#
#
# def bfs(x_s, y_s):
#     visit = [[0] * M for _ in range(N)]
#     queue = deque()
#     queue.append([x_s, y_s])
#     visit[x_s][y_s] = 1
#     ret = 1  # 시작점 포함
#     while queue:
#         x, y = queue.popleft()
#         if x == N - 1 and y == M - 1:
#             return visit[x][y]
#         for i1 in range(4):
#             if 0 <= x + dx[i1] < N and 0 <= y + dy[i1] < M:
#                 if arr[x + dx[i1]][y + dy[i1]] == 1 and visit[x + dx[i1]][y + dy[i1]] < visit[x][y]:
#                     queue.append([x + dx[i1], y + dy[i1]])
#                     visit[x + dx[i1]][y + dy[i1]] = visit[x][y] + 1
#
#
# print(bfs(0, 0))


N, M = map(int, input().split())
arr = [[] * M for _ in range(N)]
for i in range(N):
    arr[i].extend(map(int, list(str(input()))))
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(s_x, s_y):
    queue = deque()
    queue.append([s_x, s_y])
    visit = [[0] * M for _ in range(N)]
    ret = 0
    while queue:
        temp = deque()
        x, y = queue.popleft()
        if visit[x][y] == 0:
            visit[x][y] = 1
            ret += 1
        if x == N - 1 and y == M - 1:
            return ret
        for d in range(4):
            if 0 <= x + dx[d] < N and 0 <= y + dy[d] < M:
                if visit[x + dx[d]][y + dy[d]] == 0 and arr[x + dx[d]][y + dy[d]] == 1:
                    temp.append([x + dx[d], y + dy[d]])
        queue = temp


print(bfs(0, 0))
