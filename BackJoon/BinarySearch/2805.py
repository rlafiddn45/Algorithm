import sys
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
left, right = 1, max(trees)

while left <= right:
    length, mid = 0, (left + right) // 2
    for tree in trees:
        if tree >= mid:
            length += tree - mid
    if length >= M:
        left = mid + 1
    elif length < M:
        right = mid - 1


print(right)
