def solution(s):
    answer, idx = '', 0
    dicts = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    while idx < len(s):
        if s[idx] in dicts.values():
            answer += s[idx]
            idx += 1
        else:
            temp = ''
            while temp not in dicts.keys():
                temp += s[idx]
                idx += 1
            answer += dicts[temp]
    return int(answer)


print(solution("one4seveneight"))

