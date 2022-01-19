def solution(n, a, b):
    answer = 0
    s, e = 1, n
    while s < e:
        mid = (s + e) // 2
        if a > mid and b > mid:
            s = mid + 1
        elif a <= mid and b <= mid:
            e = mid
        else:
            break
        n = n // 2
    while n > 1:
        n = n // 2
        answer += 1
    return answer


print(solution(8, 1, 8))
