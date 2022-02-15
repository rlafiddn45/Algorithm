# import sys
# N = int(sys.stdin.readline())
# arr_N = list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# arr_M = list(map(int, sys.stdin.readline().split()))
#
#
# def binary_search(target, src):
#     answer = []
#     target.sort()
#
#     for s in src:
#         check, start, end, mid = 0, 0, len(target) - 1, 0
#
#         while start <= end:
#             mid = (start + end) // 2
#             if s == target[mid]:
#                 check = 1
#                 break
#             elif s < target[mid]:
#                 end = mid - 1
#             elif s > target[mid]:
#                 start = mid + 1
#
#         cnt, left, right = 1, mid - 1, mid + 1
#         if not check:
#             cnt = 0
#         else:
#             while left >= 0 and target[left] == target[mid]:
#                 cnt, left = cnt + 1, left - 1
#             while right < len(target) and target[right] == target[mid]:
#                 cnt, right = cnt + 1, right + 1
#
#         answer.append(cnt)
#
#     return answer
#
#
# res = binary_search(arr_N, arr_M)
# print(' '.join(map(str, res)))
#
# '''
# 5
# 1 1 1 1 1
# 4
# 1 2 3 4
# '''


import sys
N = int(sys.stdin.readline())
arr_N = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
arr_M = list(map(int, sys.stdin.readline().split()))


def binary_search(target, src):
    answer = []
    target.sort()

    for s in src:
        cnt, start, end, mid = 0, 0, len(target) - 1, 0

        while start <= end:
            mid = (start + end) // 2
            print('s, start, end, mid :', s, start, end, mid)
            if s == target[mid]:
                print('s, target[mid + 1] :', s, target[mid + 1])
                cnt += 1
                left, right = mid - 1, mid + 1
                while left >= start and target[left] == s:
                    cnt, left = cnt + 1, left - 1
                while right <= end and target[right] == s:
                    cnt, right = cnt + 1, right + 1
                break
            elif s < target[mid]:
                end = mid - 1
            elif s > target[mid]:
                start = mid + 1

        answer.append(cnt)

    return answer


res = binary_search(arr_N, arr_M)
print(' '.join(map(str, res)))

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
