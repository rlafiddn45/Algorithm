def to_postfix_notation(char_list):
    """
    1) 피연산자가 들어오면 바로 res 에 담는다
    2) 연산자가 들어오면 자기보다 우선순위가 높거나 같은 것들을 빼고 자신을 stack 에 담는다
    3) "(" 를 만나면 무조건 stack 에 담는다
    4) ")" 를 만나면 "(" 를 만날 때까지 stack 에서 pop 해 res 에 담는다
    5) stack 에 남은 값들을 pop 하여 res 에 담는다
    """
    priority = {"*": 2, "/": 2, "+": 1, "-": 1, "(": 0}
    res = []
    stack = []
    for char in char_list:
        if char.isnumeric():  # 피연산자 -> res
            res.append(char)
        else:
            if char == '(':
                stack.append(char)
            elif char == ')':
                while stack[-1] != '(':
                    res.append(stack.pop())
                stack.pop()
            else:
                while stack and priority[stack[-1]] >= priority[char]:
                    res.append(stack.pop())
                stack.append(char)
    while stack:
        res.append(stack.pop())
    # print("res :", res)
    return res


def calculate(char_list):
    """
    1. 피연산자를 만나면 stack 에 담는다
    2. 연산자를 만나면 stack 에서 2 개의 피연산자를 꺼내서 연산한 뒤에 stack 에 담는다
    3. 연산 후 마지막 남은 피연산자가 결과다
    4. 표기법이 틀린 경우는 들어오지 않게 만든다
    """
    stack = []
    for char in char_list:
        # print("stack :", stack)
        if char.isnumeric():
            stack.append(int(char))
        else:
            n1, n2 = stack.pop(), stack.pop()
            if char == '+':
                stack.append(n2 + n1)
            elif char == '-':
                stack.append(n2 - n1)
            elif char == '*':
                stack.append(n2 * n1)
            elif char == '/':
                if n1 != 0:  # 0으로 나누는 경우 제외
                    stack.append(n2 // n1)
                else:
                    return 0
    return stack[0]


def solution(N, number):
    answer = 9
    cnt = 0

    def check(char_list, n, left, right):
        nonlocal answer, cnt
        # cnt += 1
        # if cnt > 1000:
        #     return
        # print('char_list :', char_list)
        if n > 8:
            answer = -1
            return
        else:
            if left == right:
                if char_list == ['5', '+', '5', '+', '(', '5', '/', '5', ')', '+', '(', '5', '/', '5', ')']:
                    print('normal case :', char_list)
                temp = calculate(to_postfix_notation(char_list))
                # print('temp, number :', temp, number)
                if temp == number:
                    answer = min(temp, n)
                    return

            check(['('] + char_list, n + 1, left + 1, right)
            if left > right:
                check(char_list + [')'], n + 1, left, right + 1)
            check(char_list + ['+', str(N)], n + 1, left, right)
            check(char_list + ['-', str(N)], n + 1, left, right)
            check(char_list + ['*', str(N)], n + 1, left, right)
            check(char_list + ['/', str(N)], n + 1, left, right)
            if char_list[-1].isnumeric():
                char_list[-1] = char_list[-1] + str(N)
                check(char_list, n + 1, left, right)



    check([str(N)], 1, 0, 0)
    # print(calculate(to_postfix_notation(['55', '/', '5', '+', '5', '/', '5'])))
    # print(calculate(to_postfix_notation(['(', '55', '+', '5', ')', '/', '5'])))

    return answer


print(solution(5, 12))


'''
1 <= N <= 9
1 <= number <= 32000
수식에는 괄호와 사칙연산만 가능하고, 나누기 연산에서 나머지는 무시
최소값이 8보다 크면, -1을 return 한다

1. 더하기 2. 빼기 3. 곱하기 4. 나누기 5. 붙이기 6. 괄호
'''