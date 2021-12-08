def solution(answers):
    answer = []
    students = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    idx, ret = [0, 0, 0], [0, 0, 0]
    for j in range(len(answers)):
        for i in range(3):
            if students[i][idx[i]] == answers[j]:
                ret[i] += 1
            idx[i] += 1
            if idx[i] >= len(students[i]):
                idx[i] = 0
    for i in range(3):
        if ret[i] == max(ret):
            answer.append(i + 1)
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
