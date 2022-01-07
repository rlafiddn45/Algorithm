def solution(msg):
    answer = []
    indexes = {chr(i): i - 64 for i in range(65, 91)}
    idx, n = 0, 26
    while idx < len(msg):
        temp = msg[idx]
        while temp in indexes.keys():
            idx += 1
            if idx == len(msg):
                break
            temp += msg[idx]
        n += 1
        if temp not in indexes.keys():
            indexes[temp] = n
            if len(temp) > 1:
                temp = temp[:-1]
        answer.append(indexes[temp])
    return answer


# print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
