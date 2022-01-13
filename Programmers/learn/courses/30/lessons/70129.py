def change(x):
    n = len(''.join(list(x.split('0'))))
    ret_zero = len(x) - n
    binary = []
    while n > 0:
        binary.append(n % 2)
        n = n // 2
    result = ''.join(map(str, binary[::-1]))
    return result, ret_zero


def solution(s):
    number, n, zero = s, 0, 0
    while number != '1':
        ret_n, ret_zero = change(number)
        n += 1
        zero += ret_zero
        number = ret_n
    return [n, zero]


print(solution("110010101001"))
