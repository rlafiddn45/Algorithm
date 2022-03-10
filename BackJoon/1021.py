n, m = map(int, input().split())
arr = list(map(int, input().split()))
numbers = [i for i in range(1, n + 1)]
answer = 0


def left(array, v):
    cnt = 0
    while array[0] != v:
        array = array[1:] + [array[0]]
        cnt += 1
    return array, cnt


def right(array, v):
    cnt = 0
    while array[0] != v:
        array = [array[len(array) - 1]] + array[:len(array) - 1]
        cnt += 1
    return array, cnt


for a in arr:
    arr1, cnt1 = left(numbers, a)
    arr2, cnt2 = right(numbers, a)
    if cnt1 <= cnt2:
        numbers = arr1
    else:
        numbers = arr2
    answer += min(cnt1, cnt2)
    numbers.pop(0)
    # print('answer, numbers :', answer, numbers)


print(answer)
