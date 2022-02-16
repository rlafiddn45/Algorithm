import sys
N = int(sys.stdin.readline())
arr_n = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr_m = list(map(int, sys.stdin.readline().split()))


arr_n.sort()  # 이분 탐색을 위해 정렬
answer = []

for m in arr_m:
    left, right = 0, N - 1
    x, y = 0, 0
    while left <= right:
        mid = (left + right) // 2
        if arr_n[mid] >= m:
            right = mid - 1
        elif arr_n[mid] < m:
            left = mid + 1
    x = left
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) // 2
        if arr_n[mid] <= m:
            left = mid + 1
        elif arr_n[mid] > m:
            right = mid - 1
    y = left
    answer.append(y - x)


print(' '.join(map(str, answer)))

'''
5
1 1 1 1 1
4
1 2 3 4
'''

'''
-10 -10 2 3 3 6 7 10 10 10

10 9 -5 2 3 4 5 -10
'''

'''
8
10 9 -5 2 3 4 5 -10
8
10 9 -5 2 3 4 5 -10
'''

# -10 -5 2 3 4 5 9 10
