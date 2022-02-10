from itertools import permutations


def change(expression):
    arr, idx, temp = [], 0, ''
    while idx < len(expression):
        if expression[idx].isnumeric():
            temp += expression[idx]
        else:
            arr.append(temp)
            arr.append(expression[idx])
            temp = ''
        idx += 1
    arr.append(temp)
    return arr


def cal(x, y, c):
    x, y = int(x), int(y)
    if c == '+':
        return str(x + y)
    elif c == '-':
        return str(x - y)
    elif c == '*':
        return str(x * y)


def sol(arr, s):
    idx, ret = 0, []
    while idx < len(arr):
        if arr[idx] == s:
            idx += 1
            ret[-1] = cal(ret[-1], arr[idx], s)
        else:
            ret.append(arr[idx])
        idx += 1
    return ret


def solution(expression):
    answer = 0
    cases = []
    for e in expression:
        if not e.isnumeric() and e not in cases:
            cases.append(e)
    expression = change(expression)
    perms = list(permutations(cases, len(cases)))
    for perm in perms:
        temp = expression
        perm = list(perm)
        for p in perm:
            temp = sol(temp, p)
        if abs(int(temp[0])) > answer:
            answer = abs(int(temp[0]))
    return answer


print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))
