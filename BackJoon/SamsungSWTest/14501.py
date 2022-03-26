answer = 0
n = int(input())
times, prices = [], []
for i in range(n):
    t, p = map(int, input().split())
    times.append(t)
    prices.append(p)


def work(day, money):
    global answer
    # print('day, money :', day, money)
    if day == n:
        answer = max(answer, money)
    else:
        work(day + 1, money)
        if day + times[day] <= n:
            work(day + times[day], money + prices[day])


work(0, 0)
print(answer)
