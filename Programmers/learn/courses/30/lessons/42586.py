from collections import deque


def solution(progresses, speeds):
    answer = []
    progresses_queue, speeds_queue = deque(), deque()
    progresses_queue.extend(progresses)
    speeds_queue.extend(speeds)

    while progresses_queue:
        for i in range(len(progresses_queue)):
            progresses_queue[i] += speeds_queue[i]
        cnt = 0
        for i in range(len(progresses_queue)):
            if progresses_queue[i] >= 100:
                cnt += 1
            else:
                break
        for i in range(cnt):
            progresses_queue.popleft()
            speeds_queue.popleft()
        if cnt != 0:
            answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

# def solution(progresses, speeds):
#     answer = []
#     idx = 0
#     while idx < len(progresses):
#         temp = 0
#         while progresses[idx] < 100:
#             for i in range(idx, len(progresses)):
#                 progresses[i] += speeds[i]
#         while idx < len(progresses) and progresses[idx] >= 100:
#             temp += 1
#             idx += 1
#         answer.append(temp)
#     return answer
