def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        x = phone_book[i]
        for j in range(i + 1, len(phone_book)):
            y = phone_book[j]
            if x[0] != y[0] or len(x) > len(y):
                break
            if x == y[:len(x)]:
                return False
    return True


print(solution(["123", "456", "789"]))
