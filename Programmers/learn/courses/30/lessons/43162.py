def solution(n, computers):
    answer = 0
    visit = [0] * n

    def dfs(s):
        stack = [s]
        while stack:
            print(stack)
            x = stack.pop()
            if visit[x] == 0:
                visit[x] = 1
            for y in range(n):
                if visit[y] == 0 and computers[x][y] == 1:
                    stack.append(y)

    for i in range(n):
        if visit[i] == 0:
            dfs(i)
            answer += 1

    return answer


print(solution(3, [[1, 1, 1], [1, 1, 0], [0, 0, 1]]))

# 1 1 0
# 1 1 0
# 0 0 1
