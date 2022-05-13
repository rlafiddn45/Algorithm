"""
2차원 배열 m x n 을 나선형으로 순회해야한다.
1 2 3
8 9 4
7 6 5
"""


def spiral_traversal(m, n):
    # direction
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    # intiate array
    arr = [[0] * n for _ in range(m)]
    # make spiral_traversal clockwise
    num = 1
    x, y, d = 0, 0, 0
    while num <= m * n:
        if arr[x][y] == 0:
            arr[x][y] = num
            num += 1
        if 0 <= x + dx[d] < m and 0 <= y + dy[d] < n and arr[x + dx[d]][y + dy[d]] == 0:
            x, y = x + dx[d], y + dy[d]
        else:
            d = (d + 1) % 4
    return arr


for a in spiral_traversal(9, 9):
    print(a)
