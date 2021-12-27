from fractions import Fraction


def solution(N, stages):
    answer = []
    scores = {i: 0 for i in range(1, N + 2)}
    fails = {}
    for stage in stages:
        scores[stage] += 1
    for score in scores.keys():
        if score == N + 1:
            continue
        passed, percent = 0, 0
        for k in scores.keys():
            if k >= score:
                passed += scores[k]
        if passed:
            percent = Fraction(scores[score]/passed)
        if percent in fails.keys():
            fails[percent].append(score)
        else:
            fails[percent] = [score]
    keys = sorted([k for k in fails.keys()], reverse=True)
    for k in keys:
        answer.extend(sorted(fails[k]))
    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4]))
