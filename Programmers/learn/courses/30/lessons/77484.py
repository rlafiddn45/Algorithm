def solution(lottos, win_nums):
    answer = []
    n = 0
    for lotto in lottos:
        if lotto in win_nums:
            n += 1
    answer.append(7 - (n + lottos.count(0)))
    answer.append(7 - n)
    for i in range(len(answer)):
        if answer[i] == 7:
            answer[i] = 6
    return answer


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
