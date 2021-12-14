def solution(tickets):
    answer = []

    def bfs(cities, visit):
        if len(tickets) == sum(visit):
            answer.append(cities)
        else:
            for i in range(len(tickets)):
                if tickets[i][0] == cities[-1] and visit[i] == 0:
                    visit[i] = 1
                    bfs(cities + [tickets[i][1]], visit)
                    visit[i] = 0

    bfs(["ICN"], [0] * len(tickets))
    answer.sort()

    return answer[0]


print(solution([["ICN", "JFK"], ["JFK", "ICN"], ["ICN", "JFK"], ["JFK", "ICN"]]))
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
print(solution([["ICN", "ZZZ"], ["ZZZ", "ICN"], ["ICN", "AAC"]]))
