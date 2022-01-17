def check(string):
    stack = list(string)
    out = []
    while stack:
        char = stack.pop()
        if char in ')}]':
            out.append(char)
        else:
            if len(out) == 0:
                return False
            end = out[-1]
            if char == '(':
                if end == ')':
                    out.pop()
                else:
                    return False
            elif char == '{':
                if end == '}':
                    out.pop()
                else:
                    return False
            elif char == '[':
                if end == ']':
                    out.pop()
                else:
                    return False
    if len(out) != 0:
        return False
    return True


def solution(s):
    answer = 0
    for i in range(len(s)):
        temp = s[i:] + s[:i]
        if check(temp):
            answer += 1
    return answer


print(solution('[](){}'))
print(solution('}]()[{'))
print(solution('[)(]'))
print(solution('}}}'))
print(solution('[(])'))
