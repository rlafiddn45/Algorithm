def solution(s):
    s = s.lower()
    s = list(s)
    for i in range(len(s) - 1):
        if s[i] == ' ':
            if s[i + 1].isalpha():
                s[i + 1] = s[i + 1].upper()
    if s[0].isalpha():
        s[0] = s[0].upper()
    s = ''.join(s)
    return s


print(solution("3people unFollowed me"))
print(solution("for the last week"))
