import sys
from collections import deque


N = int(sys.stdin.readline())
queue = deque([])
for n in range(N):
    order = sys.stdin.readline().strip().split()
    c = order[0]
    if c == 'push_front':
        queue.appendleft(int(order[1]))
    elif c == 'push_back':
        queue.append(int(order[1]))
    elif c == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif c == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif c == 'size':
        print(len(queue))
    elif c == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif c == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif c == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
