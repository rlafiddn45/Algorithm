def check(x, y, arr):
    cnt = 0
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if (i + j) % 2 == (x + y) % 2:
                if arr[x][y] != arr[i][j]:
                    cnt += 1
            else:
                if arr[x][y] == arr[i][j]:
                    cnt += 1
    return min(cnt, 64 - cnt)


N, M = map(int, input().split())
board = [input() for _ in range(N)]
answer = N * M + 1
for i in range(N - 7):
    for j in range(M - 7):
        answer = min(answer, check(i, j, board))

print(answer)
