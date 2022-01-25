n = int(input())
stack, cals = [1], ['+']
i = 2
while stack or i <= n:
    number = int(input())
    while i <= number:
        stack.append(i)
        cals.append('+')
        i += 1
    last = stack.pop()
    if last == number:
        cals.append('-')
    else:
        cals.append('NO')
        break

if 'NO' in cals:
    print('NO')
else:
    for c in cals:
        print(c)
