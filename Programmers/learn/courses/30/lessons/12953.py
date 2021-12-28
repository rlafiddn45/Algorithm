def gcf(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n


def lcm(m, n):
    return m // gcf(m, n) * n // gcf(m, n) * gcf(m, n)


def solution(arr):
    answer = 1
    if len(arr) == 1:
        return arr[0]
    else:
        g, l = arr[0], arr[0]
        for i in range(len(arr)):
            g, l = gcf(g, arr[i]), lcm(l, arr[i])
        answer = l
    return answer


# print(solution([2, 6, 8, 14]))
# print(solution([1, 2, 3]))
print(solution([100, 50, 25]))
