import sys
N = int(sys.stdin.readline())
arr_N = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr_M = list(map(int, sys.stdin.readline().split()))


def binary_search(target, src):
    target.sort()

    for s in src:
        cnt, left, right = 0, 0, len(target) - 1
        while left <= right:
            mid = (left + right) // 2
            if s == target[mid]:
                cnt = 1
                break
            elif s > target[mid]:
                left = mid + 1
            elif s < target[mid]:
                right = mid - 1
        if cnt == 0:
            print(0)
        elif cnt == 1:
            print(1)


binary_search(arr_N, arr_M)
