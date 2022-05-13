def solution(x, y, d):
    sub = y - x
    if sub % d:
        return sub // d + 1
    else:
        return sub // d


print(solution(10, 85, 30))
print(solution(10, 10, 1))
print(solution(10, 20, 3))


"""
개구리는 X 에서 시작해 Y 까지 간다.
고정된 길이 D 만큼만 움직일 수 있다.
"""
