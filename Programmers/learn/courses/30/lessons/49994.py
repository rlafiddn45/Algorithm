def solution(dirs):
    answer = 0
    directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
    visit = {}
    for i in range(11):
        for j in range(11):
            visit[(i, j)] = []
    print(visit)
    x, y = 5, 5
    for d in dirs:
        next_x, next_y = x + directions[d][0], y + directions[d][1]
        if 0 <= next_x <= 10 and 0 <= next_y <= 10:
            if (next_x, next_y) not in visit[(x, y)]:
                visit[(x, y)].append((next_x, next_y))
                visit[(next_x, next_y)].append((x, y))
                answer += 1
            x, y = next_x, next_y
        print(x, y, answer)
    return answer


print(solution("LRLRLRLR"))
