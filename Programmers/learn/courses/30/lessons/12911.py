def solution(n):
    answer = []
    while n > 0:
        answer.append(n % 2)
        n = n // 2
    answer = answer[::-1]
    n = answer.count(1)
    temp = n
    while True:
        for i in range(len(answer) - 1, -1, -1):
            if answer[i] == 0:
                answer[i] = 1
                temp += 1
                break
            else:
                answer[i] = 0
                temp -= 1
        if temp == 0:
            temp = 1
            answer = [1] + answer
        if n == temp:
            break
    answer = answer[::-1]
    p, number = 0, 0
    for a in answer:
        number += a * pow(2, p)
        p += 1
    return number


print(solution(78))
