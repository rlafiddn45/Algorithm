import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def play(players):  # 순서, player, game, score
    global answer
    score = 0
    p = 0
    for g in range(N):
        out = 0
        b1, b2, b3 = 0, 0, 0  # 1루, 2루, 3루
        while out < 3:
            if arr[g][players[p]] == 0:
                out += 1
            elif arr[g][players[p]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif arr[g][players[p]] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif arr[g][players[p]] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif arr[g][players[p]] == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            p = (p + 1) % 9
    answer = max(answer, score)


perms = list(permutations([i for i in range(1, 9)], 8))
for perm in perms:
    perm = list(perm)
    ps = perm[:3] + [0] + perm[3:]
    play(ps)

print(answer)
