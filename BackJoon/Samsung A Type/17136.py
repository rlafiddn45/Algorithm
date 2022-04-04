answer = 26
arr = [list(map(int, input().split())) for _ in range(10)]
papers = [0] * 5


def check(x, y):
    global answer

    if y >= 10:
        answer = min(answer, sum(papers))
    elif x >= 10:
        check(0, y + 1)
    else:
        if arr[x][y] == 1:
            for n in range(5):
                if papers[n] == 5:
                    continue
                if x + n >= 10 or y + n >= 10:
                    continue

                sign = 1
                for i in range(x, x + n + 1):
                    for j in range(y, y + n + 1):
                        if arr[i][j] == 0:
                            sign = 0

                if sign:
                    for i in range(x, x + n + 1):
                        for j in range(y, y + n + 1):
                            arr[i][j] = 0
                    papers[n] += 1
                    check(x + n + 1, y)
                    papers[n] -= 1
                    for i in range(x, x + n + 1):
                        for j in range(y, y + n + 1):
                            arr[i][j] = 1
        else:
            check(x + 1, y)


check(0, 0)
if answer == 26:
    answer = -1
print(answer)


'''
순서를 파악하는 것이 중요하다
n x n 칸 보고 그 다음 x 좌표 아래 칸 보고 그 다음 y 좌표 오른쪽 칸을 본다
'''