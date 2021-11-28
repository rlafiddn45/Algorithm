from collections import deque

N = int(input())
B = int(input())
arr = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(B):
    m1, m2 = map(int, input().split())
    arr[m1][m2] = arr[m2][m1] = 1


def bfs(s):
    visited = [0] * (N + 1)
    queue = deque()
    queue.append(s)
    visited[s] = 1
    n = 0
    while queue:
        v = queue.popleft()
        n += 1
        for w in range(len(arr[v])):
            if arr[v][w] == 1 and visited[w] == 0:
                visited[w] = 1
                queue.append(w)
    return n - 1  # 1번 컴퓨터 제외


print(bfs(1))


# dfs 로 풀 경우
# def dfs(s):
#     n = 0
#     stack = [s]
#     visited = [0] * (N + 1)
#     while stack:
#         v = stack.pop()
#         if visited[v] == 0:
#             visited[v] = 1
#             n += 1
#         for w in range(len(arr[v])):
#             if arr[v][w] == 1 and visited[w] == 0:
#                 stack.append(w)
#     return n - 1
#
#
# print(dfs(1))