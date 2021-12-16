from collections import deque


def solution(name):
    answer = 0
    for n in name:
        temp = ord(n) - ord('A')
        answer += min(temp, 26 - temp)
    arr = deque([i for i in range(len(name)) if name[i] != 'A'])
    idx = 0
    length = len(name)
    while arr:
        if idx <= arr[0]:
            if arr[0] - idx <= length - arr[-1] + idx:
                temp = arr.popleft()
                answer += temp - idx
                idx = temp
            else:
                temp = arr.pop()
                answer += length - temp + idx
                idx = temp
        elif idx >= arr[-1]:
            if idx - arr[-1] <= length - idx + arr[0]:
                temp = arr.pop()
                answer += idx - temp
                idx = temp
            else:
                temp = arr.popleft()
                answer += length - idx + temp
                idx = temp

    return answer


print(solution("ZZAAAZZ"))
# print(solution("ZZZAAAZ"))
# print(solution("JEROEN"))
# print(solution("BBAAAAAAAB"))
# print(solution("A"))
# print(solution("AAAAAAA"))
# print(solution("ABC"))
# print(solution("AAABA"))

