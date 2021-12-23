def solution(x):
    arr = list(map(int, list(str(x))))
    return x % sum(arr) == 0


print(solution(10))
