def solution(brown, yellow):
    for i in range(yellow, 0, -1):
        j = 0
        if yellow % i == 0:
            j = int(yellow / i)
            if (i + 2) * (j + 2) == (brown + yellow):
                return [i + 2, j + 2]


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))
