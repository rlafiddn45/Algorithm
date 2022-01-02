def solution(s):
    s = list(map(int, s.split()))
    s.sort()
    return ' '.join(map(str, [s[0], s[-1]]))


print(solution("-1 2 3 -4"))
