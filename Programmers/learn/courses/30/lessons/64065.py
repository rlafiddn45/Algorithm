def change(string):
    string = string[2:-2]
    string = string.split('},{')
    for i in range(len(string)):
        string[i] = string[i].split(',')
    string.sort(key=lambda x: len(x))
    return string


def solution(s):
    answer = []
    tuples = change(s)
    for t in tuples:
        for i in t:
            if i not in answer:
                answer.append(i)
    answer = list(map(int, answer))
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
