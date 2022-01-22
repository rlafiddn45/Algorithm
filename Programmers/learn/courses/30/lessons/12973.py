def solution(s):
    answer = 1
    stack = []
    for char in s:
        if stack:
            if stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)
    if stack:
        answer = 0
    return answer


print(solution('baabaa'))
print(solution('abcda'))
