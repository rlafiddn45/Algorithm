def solution(record):
    answer = []
    users = {}
    for r in record:
        if r.split()[0] == 'Leave':
            answer.append([r.split()[1], "님이 나갔습니다."])
        else:
            status, id, name = r.split()
            users[id] = name
            if status == 'Enter':
                answer.append([id, "님이 들어왔습니다."])
    for i in range(len(answer)):
        answer[i] = users[answer[i][0]] + answer[i][1]
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
