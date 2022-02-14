# def solution(stones, k):
#     answer = 200000001
#     stones = stones + [200000001]
#     idx, i, stone, cnt, max_number = 0, 0, 200000001, 0, 0
#     while i < len(stones):
#         # print('stone, i :', stone, i)
#         if stones[i] >= stone:  # 만약 값이 더 크면 변경
#             idx, stone, cnt, max_number = i, stones[i], 0, 0
#         else:  # 값이 더 작으면 cnt + 1
#             if stones[i] > max_number:
#                 max_number = stones[i]
#             cnt += 1
#         # print('i, cnt :', i, cnt)
#         if cnt == k:  # cnt 가 개수만큼 채워졌다면
#             # print('i :', i)
#             # print('max_number :', max_number)
#             if stones[i + 1] >= max_number:  # 마지막 징검다리 + 1 도 사잇돌 중 최대값보다 크다면
#                 if answer > max_number:  # 만약 answer 보다 값이 작다면
#                     answer = max_number  # answer = 최소값
#                 stone = stones[i]
#             else:
#                 i = idx
#                 stone = stones[i + 1]
#             cnt, max_number = 0, 0
#         i += 1
#     return answer


def solution(stones, k):
    answer = 0
    start, end = 0, 200000001
    while start <= end:
        mid = (start + end) // 2
        arr = [stone - mid for stone in stones]
        cnt = 0
        for a in arr:
            if a <= 0:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                break
        if cnt < k:
            start = mid + 1
        else:
            answer = mid
            end = mid - 1
    return answer


# print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))  # 3
# print(solution([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3))  # 1
# print(solution([2, 4, 5, 3, 2, 1, 5, 2, 2, 1, 4], 3))  # 2
# print(solution([2, 2, 5], 2))  # 2
# print(solution([2, 5, 5, 5, 2], 3))  # 5
# print(solution([2, 4, 5, 3, 2, 1, 4], 3))  # 3
# print(solution([2, 2, 2, 5, 5, 5, 1, 1, 1], 3))  # 1
# print(solution([2, 4, 6, 5, 4, 3, 2, 7, 1, 2], 3))  # 4
print(solution([i for i in range(1, 200000001)], 3))
