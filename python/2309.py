heights = []
for i in range(9):
    heights.append(int(input()))

sum_height = sum(heights)

a, b = 0, 0

for i in range(9):
    for j in range(i + 1, 9):
        if sum_height - heights[i] - heights[j] == 100:
            a, b = heights[i], heights[j]

heights.remove(a)
heights.remove(b)
heights.sort()

for i in range(7):
    print(heights[i])
