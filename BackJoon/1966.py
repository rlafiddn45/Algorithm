import sys
T = int(sys.stdin.readline().strip())
for case in range(T):
    files, idx = map(int, sys.stdin.readline().strip().split())
    queue = list(map(int, sys.stdin.readline().strip().split()))
    visit = [0] * files
    p, rank = 0, 0
    while visit[idx] == 0:
        m, rank = 0, rank + 1
        for i in range(len(queue)):
            if visit[i] == 0 and queue[i] > m:
                m = queue[i]
        while True:
            if queue[p] == m:
                break
            p = (p + 1) % files
        visit[p] = rank
        p = (p + 1) % files
    print(visit[idx])
