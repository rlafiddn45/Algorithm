from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(n)]
visit = [[[0, 0] for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1


def bfs(p, q):
    queue = deque([[p, q, 0]])
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while queue:
        x, y, c = queue.popleft()  # x 좌표, y 좌표, 현재 좌표에서 벽을 뚫었는지에 대한 여부
        if x == n - 1 and y == m - 1:
            return visit[x][y][c]
        for d in range(4):
            next_x, next_y = x + dx[d], y + dy[d]
            if 0 <= next_x < n and 0 <= next_y < m:
                if maps[next_x][next_y] == 1 and c == 0:
                    visit[next_x][next_y][1] = visit[x][y][0] + 1
                    queue.append([next_x, next_y, 1])
                elif maps[next_x][next_y] == 0 and visit[next_x][next_y][c] == 0:
                    visit[next_x][next_y][c] = visit[x][y][c] + 1
                    queue.append([next_x, next_y, c])
    return -1


answer = bfs(0, 0)

print(answer)

'''
6 4
0100
1110
1000
0000
0111
0000
'''