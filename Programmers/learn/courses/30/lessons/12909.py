def solution(s):
    s = list(s)
    cnt = 0
    while s:
        char = s.pop()
        if char == ')':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    if cnt != 0:
        return False
    return True


print(solution("()())"))
