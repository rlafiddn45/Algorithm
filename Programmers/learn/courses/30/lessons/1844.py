from collections import deque


def solution(maps):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    n, m = len(maps), len(maps[0])  # 세로, 가로
    visit = [[0] * m for _ in range(n)]

    def bfs():
        queue = deque([[0, 0]])
        while queue:
            x, y = queue.popleft()
            if visit[x][y] == 0:
                visit[x][y] = 1
            for i in range(4):
                temp_x, temp_y = x + dx[i], y + dy[i]
                if 0 <= temp_x < n and 0 <= temp_y < m:
                    if maps[temp_x][temp_y] == 1:
                        if visit[temp_x][temp_y] == 0 or visit[temp_x][temp_y] > visit[x][y] + 1:
                            visit[temp_x][temp_y] = visit[x][y] + 1
                            queue.append([temp_x, temp_y])

    bfs()

    answer = visit[len(maps) - 1][len(maps[0]) - 1]
    if answer == 0:
        answer = -1
    return answer


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
