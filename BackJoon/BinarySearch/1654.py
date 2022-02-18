import sys
N, K = map(int, sys.stdin.readline().split())
lines = []
for n in range(N):
    line = int(sys.stdin.readline())
    lines.append(line)
min_line = max(lines)

cnt, left, right = 0, 1, min_line
while left <= right:
    cnt = 0
    mid = (left + right) // 2
    for line in lines:
        cnt += line // mid
    if cnt < K:
        right = mid - 1
    elif cnt >= K:
        left = mid + 1

print(right)

'''
802 / 743 / 457 / 539
4 11
505
202
202
202
'''

