def solution(N, number):
    answer = -1
    dp = [[] for _ in range(9)]
    for i in range(1, 9):
        dp[i].append(int(str(N) * i))
        for j in range(1, i):
            for front in dp[j]:
                for back in dp[i - j]:
                    dp[i].append(front + back)
                    dp[i].append(front - back)
                    dp[i].append(front * back)
                    if back:
                        dp[i].append(front // back)
        dp[i] = list(set(dp[i]))
        if number in dp[i]:
            answer = i
            break
    return answer


print(solution(5, 12))

'''
5개를 써서 연산한 경우는
(1, 4) (2, 3) (3, 2) (4, 1) 해당 연산건만큼 짝지어서 재 연산하는 것
'''