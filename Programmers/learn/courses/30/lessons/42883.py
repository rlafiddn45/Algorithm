def solution(number, k):
    answer = ['0']
    cnt, maximum = -1, '0'
    for num in number:
        if answer[-1] < num:
            idx = 0
            while answer and answer[-1] < num and cnt + idx < k:
                answer.pop()
                idx += 1
            cnt += idx
        answer.append(num)
    if cnt < k:
        for _ in range(k - cnt):
            answer.pop()
    answer = ''.join(answer)
    return answer


# print(solution("4171285439", 3))
print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))
print(solution("334", 2))
print(solution("332", 2))
print(solution("17325645", 5))

