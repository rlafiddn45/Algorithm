def check(arr, p, q, n):
    temp = 0
    # print('p, q, n :', p, q, n)
    for i in range(p, p + n):
        for j in range(q, q + n):
            temp += arr[i][j]
    if temp == 0:
        return 0
    elif temp == n * n:
        return 1
    else:
        return -1


def solution(arr):
    zero, one = 0, 0

    def reduce(x, y, d):
        nonlocal zero, one
        # print('d, zero, one :', d, zero, one)
        if d == 0:
            return
        else:
            dx = [0, 0, 1, 1]
            dy = [0, 1, 0, 1]
            for i in range(4):
                val = check(arr, x + dx[i] * d, y + dy[i] * d, d)
                # print('i, val :', i, val)
                if val == 0:
                    zero += 1
                elif val == 1:
                    one += 1
                else:
                    reduce(x + dx[i] * d, y + dy[i] * d, d // 2)

    whole = check(arr, 0, 0, len(arr))
    if whole == 0:
        zero += 1
    elif whole == 1:
        one += 1
    else:
        reduce(0, 0, len(arr) // 2)
    return [zero, one]


print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 1], [0, 1, 0, 0, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 1, 1, 1, 1]]))
