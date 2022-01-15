def check(arr, x, y):
    if x >= len(arr) or y >= len(arr) or arr[x][y] != 0:
        return False
    else:
        return True


def move(arr, x, y, d):
    dx = [1, 0, -1]
    dy = [0, 1, -1]
    n = len(arr)
    temp_x, temp_y = x + dx[d], y + dy[d]
    if not check(arr, temp_x, temp_y):
        d = (d + 1) % 3
    return x + dx[d], y + dy[d], d


def solution(n):
    answer = []
    arr = [[0] * i for i in range(1, n + 1)]
    x, y, d = 0, 0, 0  # 좌표, 방향
    for i in range(1, (n + 1) * n // 2 + 1):
        arr[x][y] = i
        x, y, d = move(arr, x, y, d)
    for a in arr:
        answer += a
    return answer


print(solution(4))
# print(solution(5))
# print(solution(6))
