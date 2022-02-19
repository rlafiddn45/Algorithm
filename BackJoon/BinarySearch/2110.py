import sys
N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline()) for _ in range(N)]
houses.sort()

left, right = 1, houses[-1] - houses[0]
while left <= right:
    mid = (left + right) // 2
    cnt = 1
    wifi = houses[0]
    for i in range(1, len(houses)):
        if houses[i] - wifi >= mid:
            cnt += 1
            wifi = houses[i]
    if cnt >= C:
        left = mid + 1
    elif cnt < C:
        right = mid - 1

print(right)


'''
9 4
1 2 3 4 5 6 7 8 9
1   3       7   9
'''
