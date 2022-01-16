def solution(word):
    answer, k = 0, 0
    string = 'AEIOU'
    arr = []

    def backtracking(w):
        arr.append(w)
        if len(w) < 5:
            for s in string:
                backtracking(w + s)
            if answer != 0:
                return

    backtracking('')

    return arr.index(word)


print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))
print(solution("UUUUU"))
