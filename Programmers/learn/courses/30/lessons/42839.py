from itertools import permutations


def solution(numbers):
    answer, perms = 0, []
    numbers = list(numbers)
    for n in range(1, len(numbers) + 1):
        perms.extend(list(permutations(numbers, n)))
    nums = set(list(int(''.join(perm)) for perm in perms))
    for num in nums:
        if num >= 2:
            for i in range(2, int(pow(int(num), 0.5)) + 1):
                if int(num) % i == 0:
                    break
            else:
                answer += 1
    return answer


print(solution("17"))
print(solution("011"))
print(solution("1234567"))
