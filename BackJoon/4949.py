def check(sentence):
    stack = []
    for char in sentence:
        if char in '([':
            stack.append(char)
        elif char in ')]':
            if len(stack) == 0:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    if stack:
        return False
    else:
        return True


while True:
    string = input()
    if string == '.':
        break
    if check(string):
        print('yes')
    else:
        print('no')
