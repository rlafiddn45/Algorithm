N, K = map(int, input().split())
numbers = [n for n in range(1, N + 1)]
answer = []
while numbers:
    idx = (K - 1) % len(numbers)
    answer.append(numbers[idx])
    numbers = numbers[idx + 1:] + numbers[:idx]
print('<' + ', '.join(map(str, answer)) + '>')
