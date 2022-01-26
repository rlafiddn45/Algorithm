import sys
input = sys.stdin.readline


N = int(input())
queue = []
cnt = 0
for n in range(N):
    order = input().strip()
    if order.split()[0] == 'push':
        queue.append(order.split()[1])
    elif order == 'pop':
        if len(queue) - cnt != 0:
            print(queue[cnt])
            cnt += 1
        else:
            print('-1')
    elif order == 'size':
        print(len(queue) - cnt)
    elif order == 'empty':
        if len(queue) - cnt != 0:
            print('0')
        else:
            print('1')
    elif order == 'front':
        if len(queue) - cnt != 0:
            print(queue[cnt])
        else:
            print('-1')
    elif order == 'back':
        if len(queue) - cnt != 0:
            print(queue[-1])
        else:
            print('-1')

