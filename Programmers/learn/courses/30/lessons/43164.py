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
    return sorted(answer)[0]


print(solution([["ICN", "SFO"], ["ICN", "ABC"], ["SFO", "ICN"]]))
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))











'''
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
'''


'''
1. 출발지로 시작하는 항공편이 있는지 확인한다
2. 여러개라면 방문했는지 and 알파벳을 확인한다
3. 방문했음을 체크한 뒤 위 내용을 반복한다
'''