from itertools import combinations


def check(rows, cols):
    tuples = []
    for row in rows:
        temp = []
        for col in cols:
            temp.append(row[col])
        tuples.append(temp)
    for t in tuples:
        cnt = tuples.count(t)
        if cnt > 1:
            return False
    return True


def solution(relation):
    answer = []
    n = len(relation[0])
    nums = [i for i in range(n)]
    for i in range(1, n + 1):
        combs = combinations(nums, i)
        for comb in combs:
            if check(relation, comb):
                case = ''.join(map(str, comb))
                if len(answer) == 0:
                    answer.append(case)
                else:
                    c = 0
                    for ans in answer:
                        f = 0
                        for a in ans:
                            if a not in case:
                                f = 1
                        if f == 0:
                            c += 1
                            break
                    if c == 0:
                        answer.append(case)
    return len(answer)


# print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
#                 ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))
# print(solution([["ryan", "music", "1"], ["ryan", "math", "2"], ["apeach", "music", "2"]]))
print(solution([["a", "1", "aaa", "c", "ng"], ["a", "1", "bbb", "e", "g"],
                ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]))
print(solution([['a',1,'aaa','c','ng'],['b',1,'bbb','c','g'],['c',1,'aaa','d','ng'],['d',2,'bbb','d','ng']]))

