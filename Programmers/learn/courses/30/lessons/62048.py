def get(n1, n2):
    while n2 > 0:
        n1, n2 = n2, n1 % n2
    return n1


def solution(w, h):
    num = get(w, h)
    answer = w * h - num * (w // num + h // num - 1)
    return answer


print(solution(8, 12))

