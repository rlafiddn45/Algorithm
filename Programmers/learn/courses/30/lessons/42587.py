def solution(priorities, location):
    seq = 0
    while True:
        if len(priorities) == 1:
            seq += 1
            break
        if priorities[0] >= max(priorities[1:]):
            seq += 1
            if location == 0:
                break
            else:
                location -= 1
                priorities = priorities[1:]
        else:
            temp = priorities.pop(0)
            priorities.append(temp)
            location -= 1
            if location == -1:
                location = len(priorities) - 1

    return seq


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))


# def solution(priorities, location):
#     answer = 0
#     printed = []
#     queue = [i for i in range(len(priorities))]
#     while queue:
#         temp = queue.pop(0)
#         for i in range(len(queue)):
#             if priorities[temp] < priorities[queue[i]]:
#                 queue.append(temp)
#                 break
#         else:
#             printed.append(temp)
#     answer = printed.index(location) + 1
#     return answer
#
