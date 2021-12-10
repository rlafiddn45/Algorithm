def solution(name):
    answer = 0
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for n in name:
        temp = alphabets.index(n) - 0
        answer += min(temp, 26 - temp)
    not_as = [i for i in range(1, len(name)) if name[i] != 'A']
    item = 0
    while len(not_as) > 0:
        temp = not_as.pop()
        answer += min(abs(temp - item), len(name) - temp + item)
        print('temp, item, answer : ', temp, item, answer)
        item = temp
    return answer


# print(solution("JEROEN"))
print(solution("BBAlB"))
# print(solution("A"))
# print(solution("AAAAAAA"))
# print(solution("ABC"))
