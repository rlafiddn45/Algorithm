def make(rows, columns):
    arr = [[0] * columns for _ in range(rows)]
    n = 1
    for i in range(rows):
        for j in range(columns):
            arr[i][j] = n
            n += 1
    return arr


def rotate(arr, query):
    num = len(arr) * len(arr[0]) + 1
    x1, y1, x2, y2 = [query[i] - 1 for i in range(4)]
    ne, se, sw, nw = arr[x1][y2], arr[x2][y2], arr[x2][y1], arr[x1][y1]
    num = min(num, ne, se, sw, nw)
    for i in range(y2, y1, -1):
        arr[x1][i] = arr[x1][i - 1]
        num = min(num, arr[x1][i])
    # print('11111111111111111111111111111111')
    # for a in arr:
    #     print(a)
    # print('22222222222222222222222222222222')
    for i in range(x2, x1, -1):
        arr[i][y2] = arr[i - 1][y2]
        num = min(num, arr[i][y2])
    # for a in arr:
    #     print(a)
    # print('33333333333333333333333333333333')
    for i in range(y1, y2):
        arr[x2][i] = arr[x2][i + 1]
        num = min(num, arr[x2][i])
    # for a in arr:
    #     print(a)
    # print('44444444444444444444444444444444')
    for i in range(x1, x2):
        arr[i][y1] = arr[i + 1][y1]
        num = min(num, arr[i][y1])
    # for a in arr:
    #     print(a)
    # print('55555555555555555555555555555555')
    arr[x1 + 1][y2], arr[x2][y2 - 1], arr[x2 - 1][y1], arr[x1][y1 + 1] = ne, se, sw, nw
    return arr, num


def solution(rows, columns, queries):
    answer = []
    arr = make(rows, columns)
    for query in queries:
        arr, num = rotate(arr, query)
        answer.append(num)
        for a in arr:
            print(a)
        print('====================================')
    return answer


print(solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))
