def make(i, n):
    # n * n 인 배열의 i 번째 row 를 반환
    arr = [i + 1] * (i + 1)
    for j in range(i + 1, n):
        arr.append(j + 1)
    return arr


def solution(n, left, right):
    answer = []
    # 1 2 3 2 2 3 3 3 3
    # 0 1 2 3 4 5 6 7 8
    # 위치 // n = 줄 수
    # x번째 줄은 [x] * x + [x + 1, x + 2, ... , n]
    if left // n == right // n:
        answer = make(left // n, n)
        temp = n * (left // n)
        return answer[left - temp: right - temp + 1]
    left_arr = make(left // n, n)
    left_arr = left_arr[left - n * (left // n):]
    answer.extend(left_arr)
    for i in range(left // n + 1, right // n):
        temp = make(i, n)
        answer.extend(temp)
    right_arr = make(right // n, n)
    right_arr = right_arr[:right - n * (right // n) + 1]
    answer.extend(right_arr)
    return answer


# print(solution(3, 2, 5))
# print(solution(4, 7, 14))
print(solution(3, 0, 0))


# [1]
# 1
# [1, 2, 2, 2]
# 1, 2, 3, 4
# [1, 2, 3, 2, 2, 3, 3, 3, 3]
# 1, 2, 3, 4, 5, 6, 7, 8, 9
# [1, 2, 3, 4, 2, 2, 3, 4, 3, 3, 3, 4, 4, 4, 4, 4]

