def change(num, n):
    arr = []
    if n <= 10:
        while num > 0:
            arr.append(num % n)
            num = num // n
    else:
        while num > 0:
            temp = num % n
            if temp < 10:
                arr.append(temp)
            else:
                arr.append(chr(55 + temp))
            num = num // n
    arr = arr[::-1]
    return ''.join(map(str, arr))


def solution(n, t, m, p):
    answer = ''
    string, number = '0', 1
    while len(string) < p + (t - 1) * m:
        string += change(number, n)
        number += 1
    for i in range(t):
        answer += string[p + i * m - 1]
    return answer


# print(solution(2, 4, 2, 1))
# print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))
