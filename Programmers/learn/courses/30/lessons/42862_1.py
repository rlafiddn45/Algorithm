def solution(n, lost, reserve):
    answer = 0
    arr = [1] * n
    for i in lost:
        arr[i - 1] -= 1
    for i in reserve:
        arr[i - 1] += 1
    for i in range(n):
        if arr[i] == 0:
            left, right = i - 1, i + 1
            if left >= 0 and arr[left] == 2:
                arr[left], arr[i] = 1, 1
            elif right < n and arr[right] == 2:
                arr[i], arr[right] = 1, 1
    print('arr :', arr)
    answer = n - arr.count(0)
    return answer
