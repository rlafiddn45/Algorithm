T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    print('Case #{}: {} + {} = {}'.format(t + 1, A, B, A + B))
