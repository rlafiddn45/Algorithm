def solution(n, lost, reserve):
    clothes = [1] * n
    for los in lost:
        clothes[los - 1] -= 1
    for rev in reserve:
        clothes[rev - 1] += 1
    for i in range(n):
        if clothes[i] == 0:
            if i == 0:
                if clothes[i + 1] == 2:
                    clothes[i] += 1
                    clothes[i + 1] -= 1
            elif i == n - 1:
                if clothes[i - 1] == 2:
                    clothes[i] += 1
                    clothes[i - 1] -= 1
            else:
                if clothes[i - 1] == 2:
                    clothes[i] += 1
                    clothes[i - 1] -= 1
                elif clothes[i + 1] == 2:
                    clothes[i] += 1
                    clothes[i + 1] -= 1
    return n - clothes.count(0)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))
print(solution(4, [2, 4], [1, 3]))
