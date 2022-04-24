def solution(id_list, report, k):
    answer = []
    declares = {}  # 신고당한 사람 모음
    for r in report:
        p1, p2 = r.split()  # 신고한 사람, 신고당한 사람
        if p2 not in declares:  # 처음 신고당했다면
            declares[p2] = [p1]
        else:  # 이미 신고 당했다면
            if p1 not in declares[p2]:  # 이 사람을 신고한 이력이 없다면
                declares[p2].append(p1)
    nums = {}  # 사용자별 받을 메일 개수
    for i in id_list:
        nums[i] = 0
    for key, value in declares.items():
        if len(value) >= k:
            for v in value:
                nums[v] += 1
    for i in id_list:
        answer.append(nums[i])
    return answer


print(solution(["muzi", "frodo", "apeach", "neo"],
               ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
'''
게시판 신고
1. 각 유저는 한 번에 한 명의 유저를 신고할 수 있다.
   - 신고 횟수에 제한은 없으나, 동일한 유저에 대한 신고 횟수는 여러 번 하더라고 1회로 처리된다.
2. k 번 이상 신고된 유저는 게시판 이용이 정지, 신고한 모든 유저에게 정지 사실을 메일로 보낸다.
   - 신고한 모든 내용을 취합해 한꺼번에 이용 정지를 시키면서 정지 메일을 발송한다.

answer : 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 return 한다.
'''
