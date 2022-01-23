from collections import deque


s, d = map(int, input().split())
visit = {}


def bfs():
    queue = deque([s])
    visit[s] = 1
    while queue:
        # print(queue, visit)
        x = queue.popleft()
        plus, minus, multiple = x + 1, x - 1, 2 * x
        if x < d:
            if plus not in visit or visit[plus] > visit[x] + 1:
                visit[plus] = visit[x] + 1
                queue.append(plus)
            if multiple not in visit or visit[multiple] > visit[x] + 1:
                visit[multiple] = visit[x] + 1
                queue.append(multiple)
        if minus >= 0:
            if minus not in visit or visit[minus] > visit[x] + 1:
                visit[minus] = visit[x] + 1
                queue.append(minus)


bfs()
print(visit[d] - 1)

#  9 17
