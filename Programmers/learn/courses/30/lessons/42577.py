def solution(phone_book):
    hash_book = {}
    for phone in phone_book:
        hash_book[phone] = 1
    for phone in phone_book:
        temp = ''
        for p in phone:
            temp += p
            if temp in hash_book and temp != phone:
                return False
    return True


print(solution(["123", "456", "789"]))
