def solution(skill, skill_trees):
    answer = 0
    inf = {skill[i]: skill[i - 1] for i in range(1, len(skill))}  # 스킬: 선행스킬
    for item in skill_trees:
        visit = {s: False for s in skill}  # 스킬: True/False
        flag = False
        for char in item:
            if char in skill:
                if char not in inf:  # 첫번째 글자는 방문 시 무조건 True
                    visit[char] = True
                else:
                    if visit[inf[char]]:
                        visit[char] = True
                    else:
                        flag = True
                        break
        if not flag:
            answer += 1
    return answer


# print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
print(solution("ABC", ["ABC"]))


