def solution(begin, target, words):
    answer = 0
    words = [begin] + words  # [begin, word1, word2 ...]
    n = len(words)
    visit = [0] * n

    def dfs():
        stack = [0]
        visit[0] = 1
        while stack:
            s = stack.pop()
            if words[s] == target:
                return visit[s] - 1
            for i in range(n):
                if visit[i] == 0 or visit[s] < visit[i]:
                    diff = 0
                    for j in range(len(words[s])):
                        if words[s][j] != words[i][j]:
                            diff += 1
                    if diff == 1:
                        stack.append(i)
                        visit[i] = visit[s] + 1
        return 0

    answer = dfs()
    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
